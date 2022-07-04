#!/usr/bin/python3
"""Module 9-rectangle
width and height plus inheritance
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class that inherits from somewhere"""

    def __init__(self, width, height):
        """instatiate the class with para width and height

        Args:
            - width: width of the rectangle
            - height: the height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.heigth = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.width, self.heigth))

    def area(self):
        """Return the area of the rectangle"""

        return self.heigth * self.width
