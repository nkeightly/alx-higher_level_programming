#!/usr/bin/python3
"""
Task 9.
Write a class Rectangle that defines a Rectangle.
Private instance attributes: width and height.
"""


class Rectangle():
    """
    class Rectangle in which width and height are
    defined as Private instance attributes.
    Args:
        width (int): horizontal side of a rectangle
        height (int): vertical side of a rectangle

    functions:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2)
        square(cls, size=0)

    Public class attribute:
        number_of_instances (int): number of instances created and not deleted
        print_symbol (any type): used to print string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization function.
        Attributes:
            width(int): horizontal side of a rectangle.
            height(int): vertical side of a rectangle.
        Public class attribute:
            number_of_instances: Incremented during each
            new instance instantiation.
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
        sym = '\n'.join([str(self.print_symbol) * self.__width
                        for rows in range(self.__height)])
        return sym

    def __del__(self):
        """
        Function that deletes an intance of Rectangle.
        Returns:
        Print the message Bye rectangle... when an instance
        of Rectangle is deleted

        Public class attribute:
            number_of_instances: Decremented during each
            instance deletion
        """
        self.__class__.number_of_instances -= 1
        print('Bye rectangle...')

    def __repr__(self):
        """
        Function that prints the string representation.
        Returns:
            String representation of the rectangle to be able
            to recreate a new instance
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Function that compairs the sizes of two rectangles.
        Returns:
            biggest rectangle based on the area. rect_1 if both have
            the same area value.
        """
        if isinstance(rect_1, Rectangle):
            pass
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle):
            pass
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Function that converts a rectangles in a square.
        Returns:
            that returns a new Rectangle instance with
            width == height == size.
        """
        return cls(size, size)
