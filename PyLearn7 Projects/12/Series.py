from Media import Media


class Series(Media):
    def __init__(self, imdb_score, n_seasons, n_episodes, director, casts, genre,
                 title, production_year, duration, url):
        super().__init__(title, production_year, duration, url)
        self.imdb_score = imdb_score
        self.n_seasons = n_seasons
        self.n_episodes = n_episodes
        self.director = director
        self.casts = casts
        self.genre = genre
