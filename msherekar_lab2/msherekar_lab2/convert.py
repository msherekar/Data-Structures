operators = ['$', '/', '*', '+', '-']
operands = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 'E', 'F']


def convert(string):
    prefix = []

    for character in string:  # reading from R>L

        if character == " ":
            print("Encountered a blank space in the prefix but it did not affect the conversion.")
            break

        if character in ["!", "@", "#", "%", "^", "&", "(", ")"]:
            print("Encountered an invalid operator" + "(" + character + ")" +
                  " in the prefix but ignored it and finished the conversion.")
            break

        if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Encountered an integer" + "(" + character + ")" +
                  "in the prefix but ignored it and finished the conversion.")
            break

        if character == "\n":
            # print("error")
            break
        if character == "\t":
            # print("error")
            break
        if character == "\r":
            print("error")
            break

        else:  # once errors have been taken care of push the remaining valid characters
            prefix.append(character)

    l = len(prefix)

    for i in range(l):

        postfix = []

        if (prefix[i] in operators) and (prefix[i + 1] not in operators) and (prefix[i + 2] not in operators):

            for j in prefix[0:i]:
                postfix.append(j)

            postfix.append(prefix[i + 1] + prefix[i + 2] + prefix[i])

            for k in prefix[i + 3:l]:
                postfix.append(k)

            # Base case
            if postfix[0] not in operators:
                return ''.join(postfix)  # this step is to convert list to string


            # Recursive call
            else:
                return ''.join(convert(postfix))





