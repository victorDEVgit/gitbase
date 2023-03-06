print("input your character name")
name = input("> ")
print(f"Hi {name} are you ready for an adventure ?")
choice = input("> ")
print("let's begin")

from sys import exit
from mod1 import gold_room
from mod1 import dead

def dragon():
    print("You are in the portal of the dragon,to get home you have to get past it.\nwhat do you do\n1. fight it\n2. talk to it")
    choice = input("> ")
    if choice == "fight":
        print("you are equipped with a special sword,strike the heart of the dragon to kill.\nThe dragon has children, what do you do.\n1. kill them all\n2. spare them")
        choice = input("> ")
        if choice == "kill":
            print("Killing it was probably better,but remember you are the intruder\nYou got innocent blood on your hand\nYou win,have a great life.")
            print("Enter the portal")
            choice = input("> ")
            print("congratulations you are back to earth")
            exit(0)
        else:
            print("Well you are not dead,the dragon has allowed you to pass\nEnter portal")
            choice = input("> ")
            print("congratulations you are back to earth, next time when you see a portal, don't enter.\nYOU WIN !!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!")
            exit(0)
    else:
        dead("It roasts you with his fire breath,dinner is served")


def wizard():
    print("You encounter a wizard who offers to help.\nBut he looks familiar.")
    print("Wizard : Do you remember me,I am the old man you helped.\nI want to repay you for your kindness.\nI have 5 bottles inside each cotains gifts I can offer you.\nChoose 1 from the five.")
    print("Choose either one, two, three, four or five")

    one = "1000 gold coin"
    two = "A wish"
    three = "Food and delicacies"
    four = "portal to earth"
    five = "Well nothing in here !"

    bottle = []
    bottle.append(one)
    bottle.append(two)
    bottle.append(three)
    bottle.append(four)
    bottle.append(five)

    choice = input("> ")

    if choice == "one":
        print(bottle[0])
        print("Well you're rich now,the old man has returned your favour.\nContinue to the next portal door.\nOpen it.")
        choice = input("> ")
        dragon()
    elif choice == "two":
        print(bottle[1])
        print("\nThink carefully for what you wish")
        choice = input("> ")
        if choice == "get out" or "earth":
            print("\nGood choice,You are back to earth\nNext time when you see a portal just keep walking.\nCongratulations \nYOU WIN !!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!")
            exit(0)
        else:
            ("\nWell you could have wished for something better.Enter portal")
            dragon()
    elif choice == "three":
        print(bottle[2])
        print("\nHope you enoyed the meal.\nYou can enter the portal now")
        dragon()
    elif choice == "four":
        print(bottle[3])
        print("\nWell you're in luck,you just redemed yourself\nEnter portal.\nWow the old man saved you.\nYou win!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!")
        exit(0)
    else:
        print(bottle[4])
        print("\nWell you are out of luck,its just like gambling,sometimes you win,sometimes you don't\nProceed")
        dragon()


def gaint():
    print("You are in the realm of the gaints.\nThey eat humans for fun.\nBut it is against the rules to kill anyone without reason.\nSo the have deviced a method to kill people.\nThey ask mind bending riddles")
    print("You have to answer three riddles.\nAre you ready ?")
    print("\nGaint : Fee Fii Foe Fum,3 riddles will you solve,miss one and become our food")
    print("\n1. He who makes me has no use of me, and he who uses me can't see me.\nWhat am I ?")
    print("\n2. The poor have me, the rich need me, if you eat me you will die.\nWhat am I")
    print("\n3. I appear once a year, twice a week and never in a month.\nWhat am I")
    riddles = True
    while True:
        choice = input("> ")
        if choice == "coffin" and riddles:
            print("Wow, you got 1 right")
        elif choice == "nothing" and riddles:
            print("Let's see if you can get the third one")
        elif choice == "e" and riddles:
            print("You have passed all the riddles,you can pass now,the gaints can't do anything to you.\nYou can now open the portal door")
            riddles = False
        elif choice == "open door" and  not riddles:
            wizard()
        else:
            dead("The gaints cuts you to pieces and shares you among themselves.")



def old_man():
    print("You encounter an old man. \nOld man : young man can you please help me carry this load to my hut. \n1. accept \n2. reject")
    choice = input("> ")
    if choice == "accept":
        print("Old man : Thank you very much,I don't have anything to give you but I hope to one day repay you for your kindness.\nI noticed you don't have a map,take this, it is a map of this forest,you need it to get out of here. ")
        print("You have arrived at the portal door,you can open it")
        choice = input("> ")
        gaint()
    else:
        dead("Old man : You can't help an old man and you expect to get out of here alive.\n\nYou continue walking for servral days and die of thirst and hunger. ")


def lion():
    print("You are in a realm of lions,but they are sleeping,what do you do to get to the other portal door ? \n 1. turn back \n 2. walk slowly past the lion \n 3. run through the field past the lion. ")
    choice = input("> ")
    if choice == "turn back":
        gold_room()
    elif choice == "walk slowly":
        print("You made it to the portal door")
        choice == ("> ")
        old_man()
    else:
        print("The lion and his packs are chasing you. \nWhat do you do ? \n1. run faster \n2. stop running")
        choice = input("> ")
        if choice == "run faster":
            dead("You cannot outrun a lion.")
        else:
            dead("You idiot why did you stop,you already started,too late.")


def warrior():
    print("In this realm you encounter a warrior who challenges you to a fight. \nWhat do you do ? \n1. accept \n2. reject ")
    choice = input("> ")
    if choice == "accept":
        print("You pinned him down to the floor with a sword to his throat. \nWhat do you do ? \n1. kill \n2. spare")
        choice = input("> ")
        if choice == "kill":
            print("BRUTALITY.Killing him was probably better.\nyou can open the portal door now.")
            choice = input("> ")
            lion()
        else:
            dead("He stabs you in your back,no mercy in the face of war.")
    else:
        dead("He stabs you twice in your back.Coward, you're dead. ")

def bear():
    print("There is a bear here, what do you do ?")
    print("1. taunt bear")
    print("2. set trap")
    choice = input("> ")

    if choice == "taunt bear":
        dead("The bear gets pissed and bites off your legs.")

    elif choice == "set trap":
        print("What type of trap do you want to set ?")
        print("1. bear cage")
        print("2. fish bait")
        print("3. honey bait")
        choice = input("> ")

        if choice == "bear cage":
            print("The bear has fallen for your trap, you can open the portal door.")
            choice = input("> ")

            if choice == "open door":
                warrior()

            else:
                dead("The bear eats you for desert.")
        else:
            dead("The bear cuts your head off,feeding the bear is not a good idea")

    else:
        dead("Not a good idea")

def enter():
    print(f"Welcome {name}, you wanted to have an adventure, but it could also cost you your life")
    print("You are far away from earth, but remember, always do the right thing.")
    print("Choose from this two portal doors,one to your right and the other to your left ?")
    choice = input("> ")
    if choice == "right":
        gold_room()
        warrior()
    elif choice == "left":
        bear()

def start():
    print(f"{name} is walking home and suddenly, sees a portal, do you enter or continue walking ? ")
    choice = input("> ")
    if choice == "enter":
        enter()
    elif choice == "walk" :
        print("I guess you weren't ready for an adventure")
    else:
        print("I know you saw the portal, you are just ignoring it.")
        print("Good luck")
start()
