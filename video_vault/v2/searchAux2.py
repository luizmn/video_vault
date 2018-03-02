import requests
import json

# Get top 10 movies from IMDB via myapifilms API
response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
top_rated = json.loads(response.content)

# Create an object with the data extracted (position in ranking, title and release year of the movie)
print "<table>"
table_toprated = {
    for item in top_rated["data"]["movies"]:
        print "<tr><td>"
        print item['ranking']
        print "</td><td>"
        print item['title']
        print "</td><td>"
        print item['year']
        print "</td></tr>"
    }
