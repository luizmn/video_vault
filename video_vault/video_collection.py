#Here you can store the information of the films

import video 
# contains classes used to define video  
import collection_listing
# creates a html page with movies/shows defined in this file


inception = video.Film("Inception",
                          "Dom Cobb (Leonardo DiCaprio) is a skilled thief,"
                          " the absolute best in the dangerous art of "
                          "extraction, stealing valuable secrets from deep"
                          " within the subconscious during the dream state,"
                          "when the mind is at its most vulnerable.",
                          "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/inception_keyart.jpg?itok=7jXiglyb", # NOQA 
                          "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                          "2010")

batman_dark = video.Film("The Dark Knight",
                          "A gang of criminals rob a Gotham City mob bank," 
                          " double-crossing and murdering each other"
                           " until only the mastermind remains: the Joker,"
                           " who escapes with the money. Batman, District"
                           " Attorney Harvey Dent and Lieutenant Jim Gordon"
                           " form an alliance to rid Gotham of organized"
                           " crime.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", # NOQA
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                          "2008")

transformers = video.Film("Transformers",
                          "Several thousand years ago, the planet Cybertron"
                          " was consumed by a civil war between the two "
                          "Transformer factions, the Autobots led by Optimus"
                          " Prime and the Decepticons led by Megatron.",
                          "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg", # NOQA
                          "https://www.youtube.com/watch?v=jkNmwrTgWdI",
                          "2007")

matrix_movie = video.Film("The Matrix",
                          "Trinity, an infamous hacker, is cornered by police"
                          " in an abandoned hotel. She overpowers them "
                          "with superhuman abilities, but a group of sinister"
                          " superhuman black-suited Agents lead the "
                          "police in a rooftop pursuit. She answers a ringing"
                          " public telephone and vanishes.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                          "1999")
                          
heat_movie = video.Film("Heat",
                          "A group of professional bank robbers start to feel"
                          " the heat from police when they unknowingly leave"
                          " a clue at their latest heist, while both sides"
                          " attempt to find balance between their personal"
                          " and professional lives.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc0YTQ5NGEtM2NkYS00MWRhLThiNzAtNmY3NWU3YzNkMjIyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,661,1000_AL_.jpg", # NOQA
                          "https://www.youtube.com/watch?v=0xbBLJ1WGwQ",
                          "1995")

lotr_movie = video.Film("The Lord of the Rings: The Two Towers",
                          "While Frodo and Sam edge closer to Mordor with the"
                          " help of the shifty Gollum, the divided fellowship"
                          " makes a stand against Sauron's new ally, Saruman,"
                          " and his hordes of Isengard.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", # NOQA
                          "https://www.youtube.com/watch?v=2dlRvAjU_RI",
                          "2002")


films = (inception, batman_dark, transformers, matrix_movie, heat_movie, 
         lotr_movie)
collection_listing.open_films_page(films)