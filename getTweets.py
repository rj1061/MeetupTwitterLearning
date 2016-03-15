import tweepy
from geopy.geocoders import Nominatim

class twitterModule:

	def __init__(self, zip_code, radius):
		self.status = False
		self.zip_code = zip_code
		self.radius = radius
		self.consumer_key = "8jVjBDg6iGrAcB9ZPsBNx0vna"
		self.consumer_secret = "8cx29BEX9bhsZaEIDgL0WKHeUGI3CPFTv3IT2CrME5GDxlNu6K"
		self.access_token ="533238162-bVotLLPj076MFD4KU54e09QLbWYmwpGoUieAFiek"
		self.access_token_secret = "Wk5MygxbFSDFke89Erm1FqzzQNOOWLPN3fjA2Px9eVmGp"

	def getTweets(self):
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		api = tweepy.API(auth)

		geolocator = Nominatim()
		location = geolocator.geocode(self.zip_code)

		geo_code = str(location.latitude) + "," + str(location.longitude) + "," + self.radius + "mi"
		public_local_tweets = api.search(lang = "en",geocode=geo_code, count=100)

		print public_local_tweets
		count = len(public_local_tweets)
		twitter_data = ""
		twitter_time = ""
		for each in range(0, count-1):
			twitter_data += public_local_tweets[each].text + " , " + "\n"

		self.status = True
		twitter_data_file = open("twitter_data.txt", "r+")
		twitter_data = twitter_data.encode('utf-8').strip()
		twitter_data_file.write(twitter_data)

		return self.status
