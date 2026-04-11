#!/usr/bin/python3
"""This module defines a Square class with size and position."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__size_pos  # position üçün daxili dəyişən

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_pos = value

    def area(self):
        """Return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # considering the position."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (position[1])
        if self.__size_pos[1] > 0:
            for _ in range(self.__size_pos[1]):
                print("")

        # Kvadratın sətirləri
        for _ in range(self.__size):
            # Soldan boşluq (position[0]) + kvadratın özü
            print(" " * self.__size_pos[0] + "#" * self.__size)
