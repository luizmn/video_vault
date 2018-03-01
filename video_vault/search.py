# -*- coding: utf-8 -*-
import requests
import json
from json2html import *

# response = requests.get("http://www.omdbapi.com/?apikey=c2968d1a&r=json&type=movie&s=matrix&y=1999")
# response = requests.get("http://www.omdbapi.com/?apikey=c2968d1a&r=json&i=tt0133093")
# comments = json.loads(response.content)
# print comments
# print "Resultado da pesquisa"
# for item in comments: 
# for item in comments["Search"]: 
    #print "Title: " + item['Title']
#    print "Release year: " + item['Year']
#    print ""


# http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0
# https://api.themoviedb.org/3/movie/top_rated?api_key=<<api_key>>&language=en-US&page=1

# Get top 10 movies from IMDB via myapifilms API
#def top_rated:
#response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
#toprated = json.loads(response.content)
#toprated = json.dumps(response.content)
toplistrated=[1, "The Shawshank Redemption", "1994", 2, "The Godfather", "1972", 3, "The Godfather: Part II", "1974", 4, "The Dark Knight", "2008", 5, "12 Angry Men", "1957", 6, "Schindler's List", "1993", 7, "Pulp Fiction", "1994", 8, "The Lord of the Rings: The Return of the King", "2003", 9, "The Good, the Bad and the Ugly", "1966", 10, "Fight Club", "1999"]
#for item in toprated["data"]["movies"]:
    #print "Title: " + item['title']
    #print "Release year: " + item['year']
    #print "Poster: " + item['urlPoster']
 #   toplistrated.append(item['ranking'])
  #  toplistrated.append(item['title'])
   # toplistrated.append(item['year'])

#toplistrated = json.dumps(toplistrated)
#print toplistrated
print "<html>"
print "<table>"
# limit =((len(toplistrated))/3)
i=0
while i < (len(toplistrated)):
    print "<tr><td>"
    print toplistrated[i]
    print "</td>"
    print "<td>"
    print toplistrated[i+1]
    print "</td>"
    print "<td>"
    print toplistrated[i+2]
    print "</td></tr>"
    i = i +3
print "</table>"
print "</html>"

