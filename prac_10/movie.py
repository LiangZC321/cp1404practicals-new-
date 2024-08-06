# TODO: Create your Movie class in this file
"""
Name: LIU SIYI
Date: 21/04/2024
"""


class Movie:
    def __init__(self, title, year):
        """
        Initializes a new instance of the Movie class.

        :param title: str - The title of the movie.
        :param year: int - The release year of the movie.
        """
        self.title = title
        self.year = year
        self.watched = False

    def __str__(self):
        """
        Returns a string representation of the movie.

        :return: str - Information about the movie.
        """
        return f"{self.title} ({self.year}) - {'Watched' if self.watched else 'Not Watched'}"

    def mark_as_watched(self):
        """
        Marks the movie as watched.
        """
        self.watched = True

    def mark_as_unwatched(self):
        """
        Marks the movie as unwatched.
        """
        self.watched = False

    pass
