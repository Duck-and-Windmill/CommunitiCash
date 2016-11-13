import urllib2
import json

response = urllib2.urlopen('https://v3v10.vitechinc.com/solr/participant/select?indent=on&q=*:*&wt=json&rows=200000')
data = json.load(response)  
with open('vitechData.json', 'w') as outfile:
	json.dump(data,outfile)
