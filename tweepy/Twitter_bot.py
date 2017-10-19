
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

access_token = "918706943593549824-Z3gQO9jTS3UMxR2b4d1YP4gRrWstELr"
access_token_secret = "Q93Y5ocsuLDKVrZIWgDkZTQaXEliO9KcikLHzpEFmpAaN"
consumer_key = "xoUFitbD6pKfkjLBkF7SVj0iw"
consumer_secret ="Lpgv9bgi2ns6wppoCyu8tX6JALe6vjAOZbxviEcaMo7S61sa2e"

class StdOutListener(StreamListener):

    def on_data(self,data):
        try:
            print(data)
            savefile = open("/Users/Srikanth/twitterdata.txt", "a")
            savefile.write(data)
            savefile.write('\n')
            return True
        except Exception as e:
            print ("Failed to write", str(e))
            time.sleep(5)

    def on_error(self,status):
        print(status)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    li = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, li)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby', 'cher', 'soccer'])
