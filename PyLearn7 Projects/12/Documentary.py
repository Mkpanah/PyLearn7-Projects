from Media import Media


class Documentary(Media):
    def __init__(self, imdb_score, director, casts, subject, title, production_year, duration, url):
        super().__init__(title, production_year, duration, url)
        self.imdb_score = imdb_score
        self.director = director
        self.casts = casts
        self.subject = subject
