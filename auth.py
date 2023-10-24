import tweepy
from env import API_KEY, API_SECRET_KEY, ACCESS_KEY, ACCESS_SECRET_KEY  # import the keys from env.py

# Authenticate to Twitter

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET_KEY)


# Create API object	
api = tweepy.API(auth, wait_on_rate_limit=True)

