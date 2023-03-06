# imports argv from system
from sys import argv
# uses argv to get a filename
script, filename = argv
# assgns open(filename) to txt
txt = open(filename)
# prints string with format
print(f"Here's your file {filename}:")
# reads filename
print(txt.read())
# prints string
txt.close()
print("Type the filename again:")
# assigns prompt to file_again
file_again = input("> ")
# assigns open(file_again) to txt_again
txt_again = open(file_again)
# reads txt
print(txt_again.read())
txt_again.close()
