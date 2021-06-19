# Name: Shivanshu Tiwari
# University Roll No: 2013507
# Semester: 6
# BTech CSE (Sec: C)
# Class Roll No: 56

# MINI PROJECT
# TOPIC:“SENTIMENT ANALYSIS ON TWITTER DATA”


import tweepy                    #Importing Libraries
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from textblob import TextBlob

class TwitterClass(object):

	def __init__(self):             #Constructor

		''' Authentication Keys '''

		consumer_key = "8AO6OU5ubyi4XO47b1C7Sjdlz"
		consumer_secret = "FS1usPrfPolvjLXbwGka5N8TWkOZhUsdxGmmTwuO016koesUSt"
		access_token = "1151573806680592384-OUFeUtpsRFZM6jQxl1AG99NEjlY0Kt"
		access_token_secret = "KKHmkHkDGVaDof8XK4fKKI52DmNl4vZlaXnx85WRfd4Lr"

		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret) #Creating Authentication object
			self.auth.set_access_token(access_token, access_token_secret) #Setting Access Token and secret
			self.api_obj = tweepy.API(self.auth)  #Creating API object
		except:
			print("Error: Authentication Failed")


	def get_sentiments(self, tweet):

		analysis = TextBlob(tweet)
		print(analysis.sentiment)

		if analysis.sentiment.polarity > 0:
			print("positive")
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			print("Neutral")
			return 'neutral'
		else:
			print("Negative")
			return 'negative'

	def get_tweets(self, query, count):         #Function for Extracting Tweets

		# empty list to store parsed tweets
		tweets = []

		try:
			tweet_data = self.api_obj.search(q = query, count = count)  #Searching

			for tweet in tweet_data:

				parsed_tweet = {}

				print(tweet.text)
				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = self.get_sentiments(tweet.text)

				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)

			return tweets

		except tweepy.TweepError as e:
			print("Error : " + str(e))

def main():

	api = TwitterClass() #Creating object

	tweets = api.get_tweets(query = 'Narendra modi', count = 100) #Getting Tweets

	negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	neutral_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
	positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

	print("\nNegative tweets percentage: {:.2f} %".format(100*len(negative_tweets)/len(tweets)))
	print("Neutral tweets percentage: {:.2f} %".format(100 * len(neutral_tweets) / len(tweets)))
	print("Positive tweets percentage: {:.2f} %".format(100*len(positive_tweets) / len(tweets)))

	''' FOR PIE CHART '''

	plt.pie([len(negative_tweets), len(neutral_tweets), len(positive_tweets)], labels=['negative', 'neutral', 'positive'], autopct="%1.1f%%")
	plt.show()

if __name__ == "__main__":
	main()
