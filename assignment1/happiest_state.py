import sys
import json
import re

us_states = [
'AL','AK','AS','AZ','AR','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MH','MD','MA','MI',
'MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY']

def hw(sent_file, tweet_file):
	scores = {}
	states = {}

	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)

	for line in tweet_file:
		tweet_score = 0.0
		tweet = json.loads(line.rstrip())
		text = tweet.get('text', '')
		words = re.findall(r"[\S']+", text)

		for word in words:
			if word in scores:
				tweet_score += scores[word]

		user = tweet.get('user')
		if user:
			location = user['location']

			state = re.findall(r"[A-Z]{2}$", location)
			if state and state[0] in us_states:
				states[state[0]] = states[state[0]] + tweet_score if state[0] in states else tweet_score

	states = sorted(states, key=states.get, reverse=True)
	print states[0]

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
