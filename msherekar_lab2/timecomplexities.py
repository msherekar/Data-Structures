import timeit
from typing import TextIO

mycode = """\

"""


print (timeit.timeit(stmt = mycode, number=1))
print (timeit.timeit(stmt = mycode, number=10))
print (timeit.timeit(stmt = mycode, number=100))