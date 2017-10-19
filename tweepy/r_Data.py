import json
import matplotlib.pyplot as plt

data_path="/Users/Srikanth/twitterdata.txt"
tweets_data =[]
tweets_file = open(data_path, 'r')

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


