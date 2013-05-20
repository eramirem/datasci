import sys
import json
import re

def hw(sent_file, tweet_file):
	new_terms = {}

	base_scores = {}
	for line in sent_file:
		term, score = line.split("\t")
		base_scores[term] = int(score)

	for line in tweet_file:
		score = 0.0

		tweet = json.loads(line.rstrip())
		text = tweet.get('text', "")
		words = re.findall(r"[\S']+", text)

		for word in words:
			if word in base_scores:
				score += float(base_scores[word])
		
		if score <> 0.0:
			for word in words:
				positive = 0
				negative = 0
				if word not in base_scores:
					if word in new_terms:
						positive = new_terms[word][0]
						negative = new_terms[word][1]

					if score > 0.0:
						positive += 1
					else:
						negative += 1

					if negative > positive:
						current = -(float(negative) / float(positive)) if positive > 0 else -(negative)
					else:
						current = (float(positive) / float(negative)) if negative > 0 else positive

					new_terms[word] = (positive, negative, float(current))
					
	for term in new_terms:
		print term.encode('utf8') , ' ' , new_terms[term][2]

		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
