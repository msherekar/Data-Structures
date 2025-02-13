"""
A class to check validity of character for converting infix to prefix. Argument is any character and returned is
    true or false. Goal is to check if each character int he given prefix string has legitimate characters i.e allowable
    characters are english alphabets and operators (/, *, $, +, -). This method will help for error handling
    :return: True or False
"""


class WhiteSpaceError(Exception):
    """Raise this error whenever white space in a prefix string"""
    pass


class OperatorError(Exception):
    """Raise this exception when an invalid operator is encountered in a prefix string"""
    pass


class IntegerError(Exception):
    """Raise this exception when an number is encountered in an prefix string"""
    pass




