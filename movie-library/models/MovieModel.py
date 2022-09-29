

class MovieModel:
    def __init__(self, title: str, description: str, categories: list, year: int, rating: int):
        self.rating: int = rating
        self.year: int = year
        self.category: list = categories
        self.description: str = description
        self.title: str = title

    def to_string2(self) ->str:
        return f"Title: {self.title} Description: {self.description} Categories: {self.category} Year: {self.year} Rating: {self.rating}"