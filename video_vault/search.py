import requests
import json


#response = requests.get("http://www.omdbapi.com/?apikey=c2968d1a&r=json&type=movie&s=matrix&y=1999")
# response = requests.get("http://www.omdbapi.com/?apikey=c2968d1a&r=json&i=tt0133093")
#comments = json.loads(response.content)
#print comments
#print "Resultado da pesquisa"
#for item in comments: 
# for item in comments["Search"]: 
    #print "Title: " + item['Title']
#    print "Release year: " + item['Year']
#    print ""


# http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0
# https://api.themoviedb.org/3/movie/top_rated?api_key=<<api_key>>&language=en-US&page=1


response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
comments = json.loads(response.content)
print comments
print "Top movies"
for item in comments["data"]: 
    print "Title: " + item['title']
#    print "Release year: " + item['year']
    print ""
