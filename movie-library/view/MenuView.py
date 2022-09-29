from services.MovieLibraryService import MovieLibraryService
from models.MovieModel import MovieModel
from ast import Num
class MenuView:
    def __init__(self):
        self.movie_library:MovieLibraryService = MovieLibraryService()
        pass

    def menu(self):
        print("Welcom to movie Library")
        print("Add movie (1)")
        print("Remove movie (2)")
        print("Show library (3)")
        print("Quit (q)")
        user_input = input("Select an option")
        self.switch_for_menu(user_input)

    def switch_for_menu(self,user_input):
        match user_input:
            case "1":
                title:str = input("Enter title")
                description:str = input("Enter description")
                categories:str = input("Enter categories")
                year:str = input("Enter year")
                rating:str = input("Enter rating")
                movie:MovieModel = MovieModel(title,description,list(categories),int(year),int(rating))
                self.movie_library.add_movie(movie)
                self.movie_library.print_all()
                pass

            case "2":

                pass
            case "3":
                self.movie_library.print_all()
                pass
            case "q":
                pass