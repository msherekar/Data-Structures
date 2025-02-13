import timeit

from typing import TextIO

mycode = """\
from msherekar_lab2.convert import convert
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for line in input_file.readlines():
    try:
        output_file.write(convert(line))
        
    except IndexError:
        output_file.write("Given prefix cannot be converted into post fix")
    
    except TypeError:
        print("None was returned")

"""


print (timeit.timeit(stmt = mycode, number=10000))
