IPackages required:

pip install requests
pip install tweepy
pip install geopy
# installing nltk
	pip install nltk
	After completion, opena  python terminal and do this
	> import nltk
	> nltk.download()
	select all packages and click install 

Objective:

The objective of this small project is to make a recommendation system for localized meetups based on the general twitter activity of the twitter users of the location.
It is an assumption that locally popular activities would reflect in the general twitter chatter at a particular location giving sufficient knowledge about the possible meetup joinees. The usage of the program is :

python learnPeoplePattern.py [zip_of_location] [radius_of_analysis]

Few Notes:
I am extremely sorry for the hacky code. The total time taken to write and minimally test is under 5 hours. The NLP used is a very basic form of analysis and will only serve the purpose of feasibility testing at most. We are limited by the twitter results since they limit the number of tweets retrieved to 100 per 15 minutes i think. For convenience I have left the results of my last run in the respective files which would be over written at the next run(ZIP_code = 10001, radius = 50). For any further questions please don’t hesitate to contact me at (908)-636-3419 or rj1061@nyu.edu.
