import requests
import json

# Get top 10 movies from IMDB via myapifilms API
response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
toprated = json.loads(response.content)

# Create an object with the data extracted (position in ranking, title and release year of the movie)
toplistrated = []
for item in toprated["data"]["movies"]:
    toplistrated.append(item['ranking'])
    toplistrated.append(item['title'])
    toplistrated.append(item['year'])

# Transform the object, removing the unicode identifier
print "passo 1"
print  toplistrated
toplistrated = json.dumps(toplistrated)
print "passo 2"
print  toplistrated
print "tamanho"
print len(toplistrated)
# Generate table with results
print "<table>"
i=0
#while i < (len(toplistrated)):
#    print "<tr><td>"
 #   print toplistrated[i]
  #  print "</td>"
 #   print "<td>"
 #   print toplistrated[i+1]
 #   print "</td>"
  #  print "<td>"
   # print toplistrated[i+2]
   # print "</td></tr>"
   # i = i +3
print "</table>"
