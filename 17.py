from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#
in_file = open(from_file)
in_data = in_file.read()
# indata = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abord.")
input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")
# closing 2 files which we opened in this program ealier
out_file.close()
in_file.close()
