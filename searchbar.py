import tweepy
import time 

apikey = "************************"
apikey_sec = "**************************"

access = "**********************************"
access_sec = "************************************"


auth = tweepy.OAuthHandler(apikey, apikey_sec)
auth.set_access_token(access, access_sec)


# Seconde
api = tweepy.API(auth)
# api.update_status('Bentilbot reporting in live!')


# hashtag = "#CodeNewbie"
tweetHandler = 10



def searchBot(HASH_TAG):
    tweets = tweepy.Cursor(api.search, HASH_TAG).items(tweetHandler)
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print("Retweet Done")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

            
# Run the function with the hashtag you want to search as parameter
searchBot("#100DaysOfCode")
searchBot("#themanbentil")
searchBot("#pukkaTech")
searchBot("#bentilzone")
