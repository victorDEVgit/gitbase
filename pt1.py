print("what is your name?", end=' ')
name = input()
print("where are you from?", end=' ')
origin = input()
print("what is your best food?", end=' ')
best_food = input()
print("who is your favourite artist?", end=' ')
artist = input()



print(f"My name is {name}, I am from {origin}, the name of my best food is {best_food}.My favourite artist is {artist} although he is dead, i love his songs. ")
from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("your name is called:", first)
print("The name of your state is:", second)
print("The name of your best food is:", third)
