#!/usr/bin/python3
"""
Task 4.
Write a class Rectangle that defines a Rectangle.
Private instance attributes: width and height.
"""


class Rectangle:
    """
    class Rectangle in which width and height are
    defined as Private instance attributes.
    Args:
        width (int): horizontal side of a rectangle
        height (int): vertical side of a rectangle

    functions:
        __init__(self, width=0, height=0)
        def width(self)
        def width(self, value)
        def height(self)
        def height(self, value)
        def area(self)
        def perimeter(self)
        def __str__(self)
        def __repr__(self)
    """
    def __init__(self, width=0, height=0):
        """
        Initialization function.
        Attributes:
            width(int): horizontal side of a rectangle.
            height(int): vertical side of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width function.
        This fuction has getter property.
        Returns:
            horizontal side of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width function.
        This fuction has setter property.
        Args:
            value: Assign width to value.
        Width must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.
        If Width is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height function.
        This fuction has getter property.
        Returns:
            vertical side of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height function.
        This fuction has setter property.
        Args:
            value: Assign height to value.
        Height must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer.
        If height is less than 0, raise a ValueError exception
        with the message size must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Function that calculates the rectangle area.
        Returns:
            rectangle area.
        """
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """
        Function that calculates the rectangle perimeter.
        Returns:
            rectangle perimeter.
        """
        perimeter = 2 * int(self.__width) + (2 * int(self.__height))

        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return perimeter

    def __str__(self):
        """
        Function that prints in stdout the rectangle
        with the character #.
        Returns:
            Rectangle with the character #.
        """
        if self.__width == 0:
            return ""
        elif self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for rows in range(self.__height)])

    def __repr__(self):
        """
        Function that prints the string representation.
        Returns:
            String representation of the rectangle to be able
            to recreate a new instance
        """
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
