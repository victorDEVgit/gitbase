from sys import argv
script, filename = argv
print("We are going to read the file you created")
open = open(filename)
print("Reading file .....")
print(open.read())
open.close()
