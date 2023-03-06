people = 40
cars = 40
trucks = 40

# checks if the variable cars is greater than people
if cars > people:
# if so it prints string
    print("We should take the cars.")
# if the above condition is not met,it checks if cars is less than people
elif cars < people:
# if so it prints string
    print ("We should not take the cars.")
#if non of the above condition is met ,it prints string
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide. ")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

bicycle = cars + people

if  bicycle > people  and bicycle < cars:
    print("The world is dominated by bicycles.")
elif cars < bicycle and people < bicycle:
    print("The world is still dominated by bicycles.")
else:
    print("that's better.")
