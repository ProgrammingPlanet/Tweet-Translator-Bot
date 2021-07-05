from tweepy import OAuthHandler,API,Stream,StreamListener
from translator import translate
import database
import json

class SL(StreamListener):
    def on_status(self, status):
        on_tweet(status)


def run_stream(api, source_user_ids):
    sl = SL()
    print('running stream.... \n')
    stream = Stream(auth = api.auth, listener=sl)
    stream.filter(follow=source_user_ids)


def on_tweet(tweet):

    print('@{} writes: {}'.format(tweet.user.screen_name, tweet.text))

    #print('retweeted_status' in tweet._json) #retweet
    #t = json.dumps(tweet._json, indent=1)
    #print(t,'\n\n')
    # return

    db = database.read()

    if tweet.user.id_str in db['translations']: # exclude other's retweet, mentions of the monitored persons

        if not 'retweeted_status' in tweet._json:   # excludes retweet by monitored user

            target = db['translations'][tweet.user.id_str]

            for lang,translators in target['languages'].items():
                for translator in translators:
                    token, secret = db['users'][translator]['access_token'], db['users'][translator]['access_token_secret']
                    post_tweet(target['username'], tweet.text, lang, token, secret, db['API_KEY'], db['API_SECRET_KEY'])


def post_tweet(user, text, lang, token, secret, api_key, api_secret):

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, secret)
    api = API(auth)
    
    _text = translate(text, lang)
    _text = '@{} ({}) \n'.format(user, lang) + _text
    api.update_status(status=_text)
    print('bot tweeted: {}'.format(_text))

