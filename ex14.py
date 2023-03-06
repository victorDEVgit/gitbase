from sys import argv

script, user_name, user_age, second  = argv
answer = '> '


print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask a few questions.")
print(f"Do you like me {user_name}?")
likes = input(answer)

print(f"Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in  {lives}. Not sure where this is.
And you have a {computer} computer. Nice.
""")


print(f"Hi it's me the {script} script again")
print(f"I would like to know your {user_age},How old are You?")
age = input(answer)

print(f"Do you have {second}?")
response = input(answer)

print("what are their names?")
names1 = input(answer)
names2 = input(answer)
names3 = input(answer)
names4 = input(answer)

print(f"What is {names1} age? ")
names1_age = input(answer)

print(f"What is {names2} age?")
names2_age = input(answer)

print(f"""
Wow!!!
I think {names1} would be the smart one,
And {names2} would be the stubborn one.
Am I right?""")
response = input(answer)

print(f"""So {names1} who is {names1_age} is senior to {names2} who is {names2_age},
Right?""")
response = input(answer)

print(f"""I think i know a lot about you now,
your name is {user_name}
you are {age}
you live in {lives}
you have {second}
one of them is named {names1} and is {names1_age},
while the other is named {names2} and is {names2_age}.
you have a {computer},
and you said {likes} about liking me""")


print("Thank you for the information.")
