import tweepy
import time

apikey = "DwritOI3StjGBKzVWXXq0D4ke"
apikey_sec = "aNweEbk1IQNyIl9hvjXkfsR6v1YwAT3XnNYwf9OtQkkRNsPUVY"

access = "1392956155614449664-MHHOm5lCnbVWS5DYNwR0NoJvKUYHaC"
access_sec = "6Pq4LyuPaFsuna3Gxa7l7gcuO4ujt0J3pT0pV08zsv4kg"


auth = tweepy.OAuthHandler(apikey, apikey_sec)
auth.set_access_token(access, access_sec)


# Seconde
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

FILE_NAME = "lastseen.txt"

# print(tweets[0].text)
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def check_mentions():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = "extended")
    for tweet in reversed(tweets):
        if("code" in tweet.full_text.lower() or "programming" in tweet.full_text.lower()):
            try:
                print(str(tweet.id)+" - "+tweet.full_text)
                api.update_status("@"+tweet.user.screen_name + " Awesome! Keep it up.", tweet.id) #comment
                api.create_favorite(tweet.id) #Like
                api.retweet(tweet.id) #retweet
                store_last_seen(FILE_NAME, tweet.id)
            except tweepy.TweepError as e:
                print(e.reason)

# retweet and like post with a hashtag
def follow_hashtag(HASH_TAG):
    tweetHandler = 10
    tweets = tweepy.Cursor(api.search, HASH_TAG).items(tweetHandler)
    for tweet in tweets:
        try:
            tweet.retweet()  #retweet
            api.create_favorite(tweet.id)  #like
            api.create_friendship(tweet.user.id)  #follow
            # time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            # time.sleep(2)
        except StopIteration:
            break

# unfollow those who unfoolows
def unfollow_unfollowers():
    for page in tweepy.Cursor(api.friends, count=100).pages():
        user_ids = [user.id for user in page]
        for relationship in api._lookup_friendships(user_ids):
            if not relationship.is_followed_by:
                print('Unfollowing @%s (%d)', relationship.screen_name, relationship.id)
                try:
                    api.destroy_friendship(relationship.id)
                except tweepy.TweepError as e:
                    print(e.reason)

# Follow all followers
def follow_followers():
    for user in tweepy.Cursor(api.followers).items():
        if not user.following:
            try:
                user.follow()
                print("User followed!")
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

# def greet_new_follower():



















def start_bot():
    while True:
        follow_followers()
        unfollow_unfollowers()
        # follow_hashtag("#themanbentil")
        # follow_hashtag("#pukkaTech")
        follow_hashtag("#bentilzone")
        time.sleep(2)



start_bot()  #starting bot