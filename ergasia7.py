import tweepy
from tweepy import OAuthHandler,API
import re
import csv

consumer_key = 'TjibAp5bpYAxstvzymEbQnV5d'
consumer_secret = 'jkzelkdJWeWR1WZ1XTxpF9XwQbpanyHajZkDjGephd6u9KaEse'
access_token = '834400938253287424-InTqCDlf3UOhqIC7tSYlmjzdBk45gGD'
access_secret = 'FworLiWeMGAlqOtsUXEcNPlBfAjrJjHyGLpuS5EW02uDf'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Epeidh vrhka pws na perasw ta tweets se txt arxeio skefthka na kanw auto kai epeita na metrhsw tis lexeis apo auto to arxeio.alla den katafera na vrw pws
def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=10)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	while len(new_tweets) < 10:
		new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	with open('%s_tweets.txt' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(outtweets)

a=raw_input("dwse username\n")
if __name__ == '__main__':
    get_all_tweets(a)


b=raw_input("dwse username\n")
if __name__ == '__main__':
    get_all_tweets(b)
