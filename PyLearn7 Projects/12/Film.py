from Media import Media


class Film(Media):
    def __init__(self, imdb_score, director, casts, genre, title, production_year, duration, url):
        super().__init__(title, production_year, duration, url)
        self.imdb_score = imdb_score
        self.director = director
        self.casts = casts
        self.genre = genre
