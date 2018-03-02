import requests
import json

toprated_tile_content = '''
<div class="col-sm-6 film-tile text-center">
        <tr>
            <td>{top_ranking}</td>
            <td>{top_title}</td>
            <td>{top_year}</td>
        </tr>
</div>
'''




# Get top 10 movies from IMDB via myapifilms API
response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=10&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")
top_rated = json.loads(response.content)

def create_toprated_tiles_content(top_rated):
top_content = ''
for item in top_rated["data"]["movies"]:
    # Append the tile for the film with its content filled in
    top_content += toprated_tile_content.format(
        top_ranking=item['ranking'],
        top_title=item['title'],
        top_year=item['year']
    )
    return top_content




