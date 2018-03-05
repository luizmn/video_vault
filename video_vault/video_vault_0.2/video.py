import webbrowser


class Film():
    """
    Creates a movie instance with all information related
    for later display. Input all the information and it
    shall outputs a complete instance
    """
    def __init__(self, film_title, film_storyline, film_poster,
                 film_trailer, film_release):
        """
        Movie information follows the pattern below:
        :param film_title: string
        :param film_storyline: string
        :param film_poster: string
        :param film_trailer: string
        :param film_release: string
        """
        self.title = film_title
        self.storyline = film_storyline
        self.poster = film_poster
        self.trailer = film_trailer
        self.release = film_release
