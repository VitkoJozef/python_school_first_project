import uzivatel
from models.MovieModel import MovieModel
from services.MovieLibraryService import MovieLibraryService
from view.MenuView import MenuView

# u = uzivatel.Uzivatel("Jan", "Jurc", 50)
# u.print_info()
she_hulk = MovieModel("She-Hulk","No desc",["abc"],2022,50)
movie_library = MovieLibraryService()
movie_library.add_movie(she_hulk)
movie_library.print_all()
menuView = MenuView()
menuView.menu()


