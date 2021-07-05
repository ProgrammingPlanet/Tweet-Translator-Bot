import tweepy

import database
from auth import sign_in

import tweet_stream


db = database.read()

auth = tweepy.OAuthHandler(db['API_KEY'], db['API_SECRET_KEY'])

source_user_ids = list(db['translations'].keys())

user = 'Language_Bot'


# access_token,access_token_secret = sign_in(auth)
access_token,access_token_secret = db['users'][user]['access_token'], db['users'][user]['access_token_secret']
# print(access_token,access_token_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


while True:
    try:
        tweet_stream.run_stream(api, source_user_ids)
    except Exception as e:
        print('Error Occured: {}'.format(e))

