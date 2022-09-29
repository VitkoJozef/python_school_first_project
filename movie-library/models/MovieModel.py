class MovieModel:
    def __init__(self, title, description, category, year, rating):
        self.category = category
        self.description = description
        self.year = year
        self.title = title
        self.rating = rating
        
    def toString(self):
