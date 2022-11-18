import tweepy

apikey = ""
apikey_sec = ""

access = ""
access_sec = ""


auth = tweepy.OAuthHandler(apikey, apikey_sec)
auth.set_access_token(access, access_sec)


# Seconde
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
