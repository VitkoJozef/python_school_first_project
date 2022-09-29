from typing import List, Any

from models.MovieModel import MovieModel


class MovieLibraryService:

    def __init__(self):
        pass

    movies: list[Any] = []

    def add_movie(self, movie: MovieModel):
        self.movies.append(movie)

    def remove_movie(self, index: int):
        self.movies.remove(index)

    def print_all(self):
        for movie in self.movies:
            print(movie.to_string2)
