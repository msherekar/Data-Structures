from Exception import OperatorError
from Exception import WhiteSpaceError

def check_character(prefix):
    for character in prefix:
        if not ((97 <= ord(character) <= 122) or (65 <= ord(character) <= 90) or (
                ord(character) in [36, 42, 43, 45, 47])):
            raise OperatorError("Invalid character in prefix string")
        elif character.isspace():
            raise WhiteSpaceError("White space encountered")
        return










