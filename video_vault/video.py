import webbrowser
        
class Film():
    # Attributes that the movie/film has 
    def __init__(self,film_title, film_storyline, film_poster, film_trailer, film_release):
        self.title = film_title
        self.storyline = film_storyline
        self.poster = film_poster
        self.trailer = film_trailer
        self.release = film_release
        
    def show_trailer(self):
        webbrowser.open(self.film_url)
