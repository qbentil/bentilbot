import tweepy

apikey = "PfxReSRMQ7ubF5qOaba3FHwia"
apikey_sec = "ERjSh9cbEMVCElI6olsCSKEN1O9jQRzBzQhKm4BF8jzrDj6bBZ"

access = "1392956155614449664-GMjI1IvZ1P5u2WnntQVB1eyqpqOzkj"
access_sec = "zZAYD1pBekJVpR6H91A0YXDvR767jbF0sAJsbEFP43FpK"


auth = tweepy.OAuthHandler(apikey, apikey_sec)
auth.set_access_token(access, access_sec)


# Seconde
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
