"""
Name: LIU SIYI
Date: 21/04/2024
Brief Project Description:
This project aims to develop a simple movie collection application using the Kivy framework in Python. 
The application allows users to add, categorize, and manage their movie collections. It utilizes JSON files for data storage and retrieval, 
providing a convenient way to store movie information locally. The user interface is designed using Kivy's declarative language, providing an intuitive 
and interactive experience for users. The application features functionality for adding new movies, sorting movies based on different criteria, 
and marking movies as watched. It also includes error handling to ensure data integrity and user feedback.
GitHub URL: https://github.com/cp1404-students/assignment-2-movies2see-2-0-WhiteDarkTarot
"""
# TODO: Create your main program in this file, using the Movies2SeeApp class

import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('app.kv')


class MovieCollection:
    def __init__(self, filename='movies.json'):
        self.filename = filename
        self.movies = []
        self.load_movies()

    def load_movies(self):
        try:
            with open(self.filename, 'r') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            self.movies = []

    def save_movies(self):
        with open(self.filename, 'w') as file:
            json.dump(self.movies, file, indent=4)

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_movies()

    def get_movies(self):
        return self.movies


class MovieApp(App):
    def build(self):
        self.movie_collection = MovieCollection()
        self.root = Builder.load_file('app.kv')
        self.update_movie_list()
        return self.root

    def add_movie(self):
        title = self.root.ids.title_input.text
        category = self.root.ids.category_input.text
        year = self.root.ids.year_input.text

        if not title or not category or not year:
            self.root.ids.status_label.text = "All fields must be completed"
            return

        if not year.isdigit():
            self.root.ids.status_label.text = "Please enter a valid number"
            return

        valid_categories = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]
        if category not in valid_categories:
            self.root.ids.status_label.text = "Invalid category selected"
            return

        movie = {'title': title, 'category': category, 'year': year, 'is_watched': False}
        self.movie_collection.add_movie(movie)
        self.clear_fields()
        self.root.ids.status_label.text = "Movie added successfully!"
        self.update_movie_list()

    def clear_fields(self):
        self.root.ids.title_input.text = ""
        self.root.ids.category_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.status_label.text = ""

    def sort_movies(self):
        sort_by = self.root.ids.sort_spinner.text
        if sort_by == 'Title':
            key_func = lambda x: x['title']
        elif sort_by == 'Category':
            key_func = lambda x: x['category']
        elif sort_by == 'Year':
            key_func = lambda x: int(x['year'])
        else:
            return  # No sorting if sort criterion is not recognized

        self.movie_collection.movies.sort(key=key_func)
        self.update_movie_list()  # Refresh the list display

    def update_movie_list(self):
        self.root.ids.movie_list.clear_widgets()
        for movie in self.movie_collection.get_movies():
            color = [0, 1, 0, 1] if movie['is_watched'] else [1, 0, 0, 1]
            button = Button(text=f"{movie['title']} ({movie['category']}, {movie['year']})", background_color=color)
            self.root.ids.movie_list.add_widget(button)

    def on_stop(self):
        self.movie_collection.save_movies()


if __name__ == '__main__':
    MovieApp().run()
