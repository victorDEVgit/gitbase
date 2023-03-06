# gets the argv package from system
from sys import argv
# uses argv
script, filename = argv
# prints string with format 'filename'
print(f"We're going to erase {filename}.")
# prints string
print("If you don't want that, hit CTRL-C (^C).")
# prints string
print("If you do want that, hit RETURN.")
# prompts answer starting with ?
input("?")
# prints string
print("Opening the file...")
# opens filename in 'write' mode and assigns it to target
target = open(filename, 'w')
# prints string
print("Truncating the file.   Goodbye!")
# empties file assigned to target
target.truncate()
# prints string
print("Now I'm going to ask you for three lines.")
# prompts user for lines
line1 = input("line 1: ")
# prompts user for lines
line2 = input("line 2: ")
# prompts user for lines
line3 = input("line 3: ")
# prints string
print("I'm going to write these to the file.")
target.write(f"""\t{line1}
\t{line2}
\t{line3}""")
# prints string
print("And finally, we close it.")
# closes target
target.close()
