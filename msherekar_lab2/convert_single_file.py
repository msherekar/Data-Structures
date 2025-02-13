from msherekar_lab2.convert import convert
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for line in input_file.readlines():
    try:
        print(convert(line))
        output_file.write(convert(line))
        output_file.write("\n")
    except IndexError:
        print("Given prefix cannot be converted into post fix")
        output_file.write("Given prefix cannot be converted into post fix")
        output_file.write("\n")
    except TypeError:
        print("None was returned")
