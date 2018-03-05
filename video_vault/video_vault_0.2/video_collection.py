# Here you can store films information
# It is divided in two main sections:
# Best seleted movies and Top 15 IMDB movies

import video
import collection_listing
import requests
import json

# First section - Selected movies
# Fill the movie information using the pattern below:
# movie_name = video.Film("Movie Name", "Storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")
# inception movie =  video.Film("movie title", "movie storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")

inception = video.Film("Inception",
                          "A thief, who steals corporate secrets through"
                          " the use of dream-sharing technology, is given"
                          " the inverse task of planting an idea into the"
                          " mind of a CEO.",
                          "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/inception_keyart.jpg?itok=7jXiglyb",  # NOQA
                          "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                          "2010")

# Batman =  video.Film("movie title", "movie storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")

batman_dark = video.Film("The Dark Knight",
                          "A gang of criminals rob a Gotham City mob bank,"
                          " double-crossing and murdering each other"
                           " until only the mastermind remains: the Joker,"
                           " who escapes with the money. Batman, District"
                           " Attorney Harvey Dent and Lieutenant Jim Gordon"
                           " form an alliance to rid Gotham of organized"
                           " crime.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                          "2008")

# Transformers =  video.Film("movie title", "movie storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")

transformers = video.Film("Transformers",
                          "An ancient struggle between two Cybertronian"
                          " races, the heroic Autobots and the evil"
                          " Decepticons, comes to Earth, with a clue to the"
                          " ultimate power held by a teenager.",
                          "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=jkNmwrTgWdI",
                          "2007")

# Matrix =  video.Film("movie title", "movie storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")

matrix_movie = video.Film("The Matrix",
                          "A computer hacker learns from mysterious rebels"
                          " about the true nature of his reality and his role"
                          " in the war against its controllers.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                          "1999")

# Heat =  video.Film("movie title", "movie storyline", "Poster URL",
#                         "Youtube trailer URL", "Release year")

heat_movie = video.Film("Heat",
                          "A group of professional bank robbers start to feel"
                          " the heat from police when they unknowingly leave"
                          " a clue at their latest heist, while both sides"
                          " attempt to find balance between their personal"
                          " and professional lives.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc0YTQ5NGEtM2NkYS00MWRhLThiNzAtNmY3NWU3YzNkMjIyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,661,1000_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=0xbBLJ1WGwQ",
                          "1995")

# The Lord of the Rings =  video.Film("movie title", "movie storyline",
#                          "Poster URL", "Youtube trailer URL", "Release year")

lotr_movie = video.Film("The Lord of the Rings: The Two Towers",
                          "While Frodo and Sam edge closer to Mordor with the"
                          " help of the shifty Gollum, the divided fellowship"
                          " makes a stand against Sauron's new ally, Saruman,"
                          " and his hordes of Isengard.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=2dlRvAjU_RI",
                          "2002")

# Set films variable with all the movies from this file
films = (inception, batman_dark, transformers, matrix_movie, heat_movie,
         lotr_movie)

# Second section - Top 15 movies
# Get top 15 movies from IMDB via myapifilms API
response = requests.get("http://api.myapifilms.com/imdb/top?start=1&end=15&token=2bc908e5-4c25-458b-8653-b4748c2b1975&format=json&data=0")  # NOQA
# Loads the response content in a variable to work later
top_content = json.loads(response.content)

collection_listing.open_films_page(films, top_content)
