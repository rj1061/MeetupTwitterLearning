import requests
import json
import nltk
from nltk.tokenize import word_tokenize

class meetupQuery:

	def __init__(self, location_zip = "", miles_to_zip = ""):
		self.location_zip = location_zip
		self.miles_to_zip = miles_to_zip
		self.api_key = "2b46297686b14683165f1bda5c6"
		self.api_host = "https://api.meetup.com"

class findGroups:

	query_type = "/find/groups?"
	argument_type = ["category",
			"country",
			"fallback_suggestion",
			"fields",
			"filter",
			"lat",
			"lon",
			"location",
			"radius",
			"self_groups",
			"text",
			"topic_id",
			"upcoming_events",
			"zip"]

	def __init__(self, category = "", country = "", fallback_suggestions = "", fields = "", filter_applied = "", lat = "", lon = "", location = "", radius = "", self_groups = "", text = "", topic_id = "", upcoming_events = "", zip_code = "", order = ""):
		self.arguments = []
		self.arguments.append(category)
		self.arguments.append(country)
		self.arguments.append(fallback_suggestions)
		self.arguments.append(fields)
		self.arguments.append(filter_applied)
		self.arguments.append(lat)
		self.arguments.append(lon)
		self.arguments.append(location)
		self.arguments.append(radius)
		self.arguments.append(self_groups)
		self.arguments.append(text)
		self.arguments.append(topic_id)
		self.arguments.append(upcoming_events)
		self.arguments.append(zip_code)

		self.order = order

	def generateQuery(self):
		meetup = meetupQuery( "11220", "50")
		query = meetup.api_host + self.query_type + "key=" + meetup.api_key
		for count in range(0, 14):
			if self.arguments[count] != "":
				query += "&" + self.argument_type[count] + "=" + self.arguments[count]
		if self.order != "":
			query += "&order=" + self.order
		query += "&sign=true"
		return query

class runMeetupQuery:
	def __init__(self, query = "", word_freq_dist = None):
		self.query = query
		self.result = requests.get(query)
		save_meetup_object = saveMeetupLearningData(self.result, word_freq_dist)
		save_meetup_object.saveToFile()
		if word_freq_dist != None:
			save_meetup_object.saveRanksToFile()
		self.returnResult()
	
	def returnResult(self):
		return True

class saveMeetupLearningData:
	def __init__(self, response, word_freq_dist):
		self.word_freq_dist = word_freq_dist
		self.response = response
		self.names = []
		self.meetup_id = []
		self.link = []
		self.urlname = []
		self.description = []
		self.members = []
		self.who = []
		self.rank = []
	
	def saveToFile(self):
		meetup_list = self.response.json()
		for data in meetup_list:
			self.names.append(data['name'])
			self.meetup_id.append(data['id'])
			self.link.append(data['link'])
			self.urlname.append(data['urlname'])
			self.description.append(data['description'])
			self.members.append(data['members'])
			self.who.append(data['who'])

		return True

	def saveRanksToFile(self):
		rank_points = 0
		for each_meetup in range(0, len(self.meetup_id)):
			description_tokenized = word_tokenize(self.description[each_meetup])
			for each_word in description_tokenized:
				rank_points += self.word_freq_dist[each_word]
			self.rank.append(rank_points)
			rank_points = 0
		rank_file = open('ranked_meetups.txt', 'r+')
		file_str = "RANK_SCORE\tMEETUP_NAME\tMEETUP_LINK\tMEETUP_URLNAME\n"
		for each_meetup in range(0, len(self.meetup_id)):
			file_str += str(self.rank[each_meetup]) + "\t" + self.names[each_meetup].encode('utf-8') + "\t" + self.link[each_meetup].encode('utf-8') + "\t" + self.urlname[each_meetup].encode('utf-8') + "\n"
		rank_file.write(file_str)

