import tweepy
import time

consumer_key = 'GAuX3Op3dkqlHLT4aVW7pLXwp'
consumer_secret = 'Yy99m5tXcpF5GIjEzzahyXF7zcb2IowrB9ErpnPtllFxeVsplV'

key = '1358799857947877376-S79gBppmqm6gocn797eXiRNSEuGNRu'
secret = 'hTeW1CUwRD2HPxNw7cSAiUNWB10l96NXFAg1MY993Z1kl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#coing10' in tweet.full_text.lower():
            print(str(tweet.id)+ ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Auto reply, like, and retwit work naka 2 :)", tweet.id)
            api.create_favorite(tweet.id) 
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(2)
    
    
