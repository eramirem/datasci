import sys
import json
import re

def hw(sent_file, tweet_file):
	scores = {}
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
		print tweet_score

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()