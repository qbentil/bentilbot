import tweepy
import time
from auth import api

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
    new_last_seen = None
    for tweet in reversed(tweets):
        if("bentilzone" in tweet.full_text.lower() or "bentilbot" in tweet.full_text.lower()):
            try:
                print(str(tweet.id)+" - "+tweet.full_text)
                api.update_status("@"+tweet.user.screen_name + " Awesome!.", tweet.id, auto_populate_reply_metadata = True) #comment
                api.create_favorite(tweet.id) #Like
                api.retweet(tweet.id) #retweet
                new_last_seen = tweet.id
            except tweepy.TweepError as e:
                print(e.reason)
        if new_last_seen:
            store_last_seen(FILE_NAME, new_last_seen)

# retweet and like post with a hashtag
def follow_hashtag(HASH_TAG):
    tweetHandler = 10
    tweets = tweepy.Cursor(api.search, HASH_TAG).items(tweetHandler)
    for tweet in tweets:
        try:
            tweet.retweet()  #retweet
            api.create_favorite(tweet.id)  #like
            # api.create_friendship(tweet.user.id)  #follow
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
    for user in tweepy.Cursor(api.get_followers).items():
        if not user.following:
            try:
                user.follow()
                print("User followed!")
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

# def greet_new_follower():

def hashTags(*args):
    for arg in args:
        follow_hashtag(arg)








def start_bot():
    while True:
        follow_followers()
        unfollow_unfollowers()
        hashTags("#100DaysOfCode", "#themanbentil", "#pukkaTech", "#bentilzone")
        check_mentions()
        time.sleep(2)



start_bot()  #starting bot