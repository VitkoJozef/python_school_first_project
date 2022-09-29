class MovieModel:
    def __init__(self, title: str, description: str, category: list, year: int, rating: int):
        self.rating: int = rating
        self.year: int = year
        self.category: list = category
        self.description: str = description
        self.title: str = title

    def to_string(self) ->str:
        return f"Title: {self.title} Description: {self.description} Categories: {self.category} Year: {self.year} Rating: {self.rating}"