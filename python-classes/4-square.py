#!/usr/bin/python3
"""
This module defines a Square class with getter and setter.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size  # Bu birbaşa setter-i çağırır

    @property
    def size(self):
        """
        Retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
