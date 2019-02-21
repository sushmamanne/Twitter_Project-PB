#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#Variables that contains the user credentials to access Twitter API 
access_token = "1097971979800530947-o65JiBKNZaWj3fjY7AykH3uMkCRiHO"
access_token_secret = "iwim6HYHMP5XGoNOwlolcqNEsDxcVgzCFKGfB5hF2nsJC"
consumer_key = "GrTZVUoUD6AOG4hpwdvwlnwSY"
consumer_secret = "lWUyw7thrb0HwRwfTx6IFb9s9VdVSZvBvzGrWNHMKuvp4W20JR"

i = 0

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        global i
        i=i+1
        print(data)
        if i ==100000:
            sys.exit()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['sports', 'movies'])

