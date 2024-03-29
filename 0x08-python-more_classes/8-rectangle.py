#!/usr/bin/python3
""" defines class rectangle """

class Rectangle:
    """
      Initializing the class

          Attributes:
              instance_count (int): Number of active instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initial parameters """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Property setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            Property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Property setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ solves for area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ solves for perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Rectangular pattern """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            if i > 0:
                rect += "\n"
            for j in range(self.__width):
                rect += str(self.print_symbol)
        return rect

    def __repr__(self):
        """
            String representation
        """
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Returns rectangle instance with biggest area
        Args:
            rect_1: First rectangle
            rect_2: Second rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

