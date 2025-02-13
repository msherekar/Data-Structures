from random import randint
from QuickSort import QuickSort

file = open("random10000.txt", "w")
for i in range(10000):
    line = str(randint(0, 10000))
    file.write(line)
    file.write("\n")

data = []
with open("random10000.txt", "r") as file:
    for line in file.readlines():
        number = int(line.strip())
        data.append(number)
print(data)

QuickSort(data, 0, len(data)-1)
print(data)

file_acs = open("ascending10000.txt", "w")
for i in range(len(data)):
    file_acs.write(str(data[i]))
    file_acs.write("\n")

data_reversed = data[::-1]
file_dcs = open("descending10000.txt", "w")
for i in range(len(data_reversed)):
    file_dcs.write(str(data_reversed[i]))
    file_dcs.write("\n")










