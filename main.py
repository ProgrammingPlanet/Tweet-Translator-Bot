import tweepy

import database
from auth import sign_in

import tweet_stream


db = database.read()

auth = tweepy.OAuthHandler(db['API_KEY'], db['API_SECRET_KEY'])

source_user_ids = db['users']['sources']
user = 'Language_Bot'

# access_token,access_token_secret = sign_in(auth)
access_token, access_token_secret = db['users']['targets'][user]['access_token'], db['users']['targets'][user]['access_token_secret']
# print(access_token,access_token_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet_stream.run_stream(api, source_user_ids)


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet._json)






#txt = 'सब इंसान बराबर हैं, चाहे वो किसी धर्म या जाति के हों। हमें ऐसा भारत बनाना है जहाँ सभी धर्म और जाति के लोगों में भाईचारा और मोहब्बत हो, न कि नफ़रत और बैर हो।'

# translation = translator.translate(txt)

# print(translation)










