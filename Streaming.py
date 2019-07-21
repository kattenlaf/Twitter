__author__ = 'Ruel Gordon'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class Listener( StreamListener ):

    def on_data( self, data ):
        try:
            tweet = data
            print(tweet)
            saveFile = open('avengers.txt', 'a')
            saveFile.write(tweet)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print('failed ondata,',str(e))
            time.sleep(10)

    def on_error(self, status):
        print(status)

auth = OAuthHandler( consumer_key, consumer_secret )
auth.set_access_token( access_token, access_secret )
keywords = ["avengers"] #Enter keywords to search for here
twitterStream = Stream( auth, Listener() )
twitterStream.filter(track=keywords)

#Stream tweets using the keyword in python2
