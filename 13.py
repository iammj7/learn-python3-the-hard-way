# in this we explore another input method to pass var
# read the WYSS section for how to run this
# import argv from py library
from sys import argv

# assigning 3 vars to argv first one is default for argv
file, first, second, third = argv

print("The script is called:", file)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
