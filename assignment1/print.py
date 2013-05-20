import urllib
import json

base_url = "http://search.twitter.com/search.json"
query = "q=microsoft"
pagination = "page="
params = "language=en"

for page in range(1, 11):
	full_url = base_url + "?" + query + "&" + pagination + str(page) + "&" + params
	response = json.load(urllib.urlopen(full_url))
	for doc in response['results']:
		print doc['text']
