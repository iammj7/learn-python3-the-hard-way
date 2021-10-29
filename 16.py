from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")
# opening file and we pass 'w ' for writing into that file
print("Opening the file")
target = open(filename, 'w')
# Erasing the file after opening
print("Truncating the file. Goodbye!")
target.truncate()
# inputing strings in 3 variables
print("Now I'm going to ask you for three line.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# writing those 3 variable strings into the file using write method
print("I'm going to write these to the file.")
target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# closing the file using close() method
print("And finally, we close it.")
target.close()
