from tweepy import OAuthHandler,API,Stream,StreamListener
from translator import translate
import database

class SL(StreamListener):
    def on_status(self, status):
        on_tweet(status)


def run_stream(api, source_user_ids):
    sl = SL()
    print('running stream.... \n')
    stream = Stream(auth = api.auth, listener=sl)
    stream.filter(follow=source_user_ids)


def on_tweet(tweet):

    # tweet = tweet._json

    print(tweet._json)
    print('\n\n')

    return

    db = database.read()

    for username,target in db['users']['targets'].items():
        if tweet.user.id_str == target['source']:
            post_tweet(tweet.text, target, db['API_KEY'], db['API_SECRET_KEY'])

    print('@{} writes: {}'.format(tweet.user.screen_name, tweet.text))


def post_tweet(text, target, api_key, api_secret):

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(target['access_token'], target['access_token_secret'])
    api = API(auth)

    for lang in target['languages']:
        _text = translate(text, lang)
        api.update_status(status=_text)
        print('tweeted: {}'.format(_text))


