import sys
import json
import re
import urllib2 as urllib

def hw(sent_file, tweet_file):
	excluded_speech = ('determiner, pronoun', 'pronoun', 'conjuction', 'conj', 'determiner', 'det', 'interjection', 'prep', 'preposition', 'definite article', 'indefinite article', 'linking word')
	new_terms = {}

	base_scores = {}
	for line in sent_file:
		term, score = line.split("\t")
		base_scores[term] = int(score)

	for line in tweet_file:
		score = 0.0

		tweet = json.loads(line.rstrip())
		text = tweet.get('text', "")
		words = re.findall(r"[\w']+", text)

		for word in words:
			if word in base_scores:
				score += float(base_scores[word])
		
		if score <> 0.0:
			for word in words:
				if word not in base_scores:
					query = "http://api.pearson.com/v2/dictionaries/entries?headword=" + word.lower() +"&apikey=3c453112a207b23627566408431986ba"

					pearson_json = json.load(urllib.urlopen(query))
					parson_array = pearson_json["results"]

					for element in parson_array:
						part_of_speech = element.get("part_of_speech", "undefined")

						if part_of_speech not in excluded_speech:
							if word in new_terms:
								count = new_terms[str(word)][0]
								current_score = new_terms[str(word)][1]

								new_score = (current_score + score) / (count + 1)
								new_terms[str(word)] = (count + 1, new_score)
							else:
								new_terms[str(word)] = (1, score)

	for term in new_terms:
		print term , ' ' , new_terms[term][1]

		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
