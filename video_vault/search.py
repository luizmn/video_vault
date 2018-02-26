import requests
import json
from pprint import pprint

response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=c2968d1a&r=json&type=movie&s=matrix")
comments = json.loads(response.content)
 
print "Resultado da pesquisa"
for item in comments["Search"]: 
    print "Title: " + item['Title']
    print "Release year: " + item['Year']
    print ""


