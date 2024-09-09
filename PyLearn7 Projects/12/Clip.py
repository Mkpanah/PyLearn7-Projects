from Media import Media


class Clip(Media):
    def __init__(self, views, uploader, title, production_year, duration, url):
        super().__init__(title, production_year, duration, url)
        self.views = views
        self.uploader = uploader
