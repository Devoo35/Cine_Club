from PySide2 import QtWidgets
from movie import get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
    
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # L E = Line Edit
        self.le_movieTitle  = QtWidgets.QLineEdit()
        self.btn_addMovie   = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            self.lw_movies.addItem(lw_item)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()