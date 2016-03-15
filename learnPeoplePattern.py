from getTweets import twitterModule
from getMeetups import findGroups, runMeetupQuery, saveMeetupLearningData
from sys import argv
import nltk
from nltk.tokenize import word_tokenize

ZIPCODE = argv[1]
RADIUS = argv[2]

twitter_object = twitterModule(zip_code = ZIPCODE, radius = RADIUS)
twitter_object.getTweets()

twitter_file = open('twitter_data.txt', 'r')
twitter_data = twitter_file.read().decode('utf-8')
tokenized_tweets = nltk.FreqDist(word_tokenize(twitter_data))

meetup_object = findGroups(radius = RADIUS, zip_code = ZIPCODE, order = "members")
query = meetup_object.generateQuery()
print query

response = runMeetupQuery(query, tokenized_tweets)
print "Tweets can be found in twitter_data.txt\n"
print "Ranks along with meetup details can be found in ranked_meetups.txt\n"
