"""
Name: LIU SIYI
Date: 21/04/2024
"""


# TODO: Create your MovieCollection class in this file

import json
from movie import Movie


class MovieCollection:

    def __init__(self):
            """
            Initializes a new instance of the MovieCollection class.
            """
            self.movies = []

    def add_movie(self, movie):
            """
            Adds a single Movie object to the movies list.

            :param movie: Movie - The movie object to add.
            """
            self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
            """
            Returns the number of unwatched movies in the collection.

            :return: int - Number of unwatched movies.
            """
            return sum(1 for movie in self.movies if not movie.watched)

    def get_number_of_watched_movies(self):
            """
            Returns the number of watched movies in the collection.

            :return: int - Number of watched movies.
            """
            return sum(1 for movie in self.movies if movie.watched)

    def load_movies(self, filepath):
            """
            Loads movies from a JSON file into the movies list.

            :param filepath: str - The path to the JSON file containing the movies.
            """
            with open(filepath, 'r') as file:
                movies_data = json.load(file)
            for movie_data in movies_data:
                self.add_movie(Movie(movie_data['title'], movie_data['year']))

    def save_movies(self, filepath):
            """
            Saves the movies from the movies list into a JSON file.

            :param filepath: str - The path to the JSON file to save the movies.
            """
            with open(filepath, 'w') as file:
                json.dump([{'title': movie.title, 'year': movie.year, 'watched': movie.watched} for movie in self.movies], file, indent=4)

    def sort(self, key):
            """
            Sorts the movies list by the specified key and then by title.

            :param key: str - The attribute of the Movie class by which to sort the list.
            """
            self.movies.sort(key=lambda movie: (getattr(movie, key), movie.title))


    pass
