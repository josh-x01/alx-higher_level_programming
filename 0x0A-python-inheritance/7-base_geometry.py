#!/usr/bin/python3
"""Module 6-base_geomery.
the set of error why? just because.
"""


class BaseGeometry:
    """The geometry class"""

    def area(self):
        """a function the raise exception in
        the middle of nowhere.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if the value is valid integer or not

        Args:
            - name: the name
            - value: the value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
