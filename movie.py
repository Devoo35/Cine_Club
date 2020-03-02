import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data","movies.json")

def get_movies():
    with open(DATA_FILE,"r") as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies

class Movie:
    def __init__(self,title):
        # .title() est la fonctionnalité qui met en majuscule à chaque mot
        self.title = title.title()

    # Permet de retourner le titre au lieu de l'adresse memoire de (m)
    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE,"w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else: 
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            


if __name__ == "__main__":
    movies = get_movies()
    print(movies)




