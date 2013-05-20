import sys
import json
import re

def hw(tweet_file):
	top_ht = {}
	count = 0

	for line in tweet_file:

		tweet = json.loads(line.rstrip())
		entities = tweet.get('entities')
		if entities:
			hashtags = entities.get('hashtags')
			if hashtags:
				for item in hashtags:
					text = item['text']

					if text in top_ht:
						top_ht[text] += 1
					else:
						top_ht[text] = 1

	sorted_top_ht = sorted(top_ht, key=top_ht.get, reverse=True)
	sorted_top_ht = sorted_top_ht[0:10]

	for item in sorted_top_ht:
		print item, ' ', top_ht[item]	

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
