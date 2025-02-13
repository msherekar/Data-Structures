with open("exp.txt") as input_file:
    for prefix in input_file:

        for character in prefix:
            try:
                # print(character)
                check_character(character)
            except OperatorError:
                print("error")
            except WhiteSpaceError:
                print("error")
            except NameError:
                print("error")

def check_character(prefix):
    for character in prefix:
        if not ((97 <= ord(character) <= 122) or (65 <= ord(character) <= 90) or (
                ord(character) in [36, 42, 43, 45, 47])):
            raise OperatorError("Invalid character in prefix string")
        elif character.isspace():
            raise WhiteSpaceError("White space encountered")
        else:
            print(" ")

with open("in.txt") as input_file:
    for prefix in input_file:
        for character in prefix:
            try:
                check_character(character)
            except OperatorError:
                print(" ")
            except WhiteSpaceError:
                print(" ")
def is_valid(character):
    if (97 <= ord(character) <= 122) or (65 <= ord(character) <= 90) or (ord(character) in [36, 42, 43, 45, 47]):
        return True
    else:
        return False

except ord(i) < 97:
print("invalid")
except ord(i) > 122:
print("invalid")
except ord(i) < 65:
print("invalid")
except ord(i) > 90:
print("invalid")
except ord(character) not in [36, 42, 43, 45, 47]:
print("invalid")
except i.ispace():
print("White space")

with open("in.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print("Prefix: " + line.rstrip())
        print("Postfix: " + convert(line) + "\n")
next_line = file.readline()
    while next_line is not None and next_line != "":
        try:
            print("Prefix: " + file.readline().strip())
            print("Postfix: " + convert(file.readline()) + "\n")

        finally:
            next_line = file.readline()
# working code
with open("in.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print("Prefix: " + line)
        print("Postfix: " + convert(line) + "\n")

example = "+-a^bc"
for i in example:
    if i == "^":
        break
    else:
        print(i)
print("************")


word = "+-a^bc"
for i in word:
    if i == "^":
        break
    print(i)
