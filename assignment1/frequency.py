import sys
import json
import re

def hw(tweet_file):
	term_frequency = {}
	count = 0

	for line in tweet_file:

		tweet = json.loads(line.rstrip())
		text = tweet.get('text', "")
		words = re.findall(r"[\S']+", text)
		count += len(words)

		for word in words:
			if word in term_frequency:
				term_frequency[word] += 1
			else:
				term_frequency[word] = 1

	for term in term_frequency:
		print term, term_frequency[term]/float(count)	

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
