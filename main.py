import uzivatel
from models.MovieModel import MovieModel
from services.MovieLibraryService import MovieLibraryService

u = uzivatel.Uzivatel("Jan", "Jurc", 50)
u.print_info()
she_hulk = MovieModel("She-Hulk","No desc",None,2022,50)
print(she_hulk.__str__)
