import requests
import json


# Get top 10 movies from IMDB via myapifilms API
response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
top_rated = json.loads(response.content)


top_content = ''

print "content"
print top_content




for item in top_rated["data"]["movies"]:
    # Append the tile for the film with its content filled in
    top_content += top_content.format(
        "<tr><td>"+str(item['ranking']),"</td><td>",str(item['title']),"</td><td>",str(item['year']),"</td></tr>"
    )

print "TOP content"
print top_content
