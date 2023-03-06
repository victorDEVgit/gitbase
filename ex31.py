print("""You enter a dark room with two doors.
Do you go through door #1 or #2?""")

door = input("> ")

if door == "1":
    print("There's a  gaint bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
        print("""What do you do now?
        1. continue walking
        2. turn back""")

        option1 = input("> ")

        if option1 =="1":
            print("You encounter a wizard who says he would grant you a wish")
            print("""What do you wish for?
            1. I wish I had my face back
            2. I wish to be out of this place""")

            reply = input("> ")
            if reply == "1":
                print("You have your face back")
                print("You continue walking for many days and die of hunger and thirst")
                print("Ask for what you need. Good luck!")
            elif reply == "2":
                print("You are teleported back to earth")
                print("You made the right coice")
                print("Game over🎉🎉🎉🎊🎊🥳🥳👏👏👍👍")



        elif option1 == "2":
            print("The bear tears you to pieces. Nice try!")
        else:
            print("Wrong move!")

    elif bear == "2":
        print("The bear eats your leg off. Good job!")
        print("You crawl deeper into the forest, and meet a wizard,")
        print("Wizard : I see you have gotten so far, tell me your wish and i will grant it to you.")
        print("What do you wish for ?")
        print("1 . I wish for all the worlds riches.")
        print("2 . I wish for more wishes.")
        print("3 . I wish that I have my legs back.")

        option2 = input("> ")
        if option2 == "1" or option2 == "2":
            print("Wizard : You have put your selfish needs before your immediate, therefore, you are sentenced to death. ")
            print("Nice try!!!")
        elif option2 == "3":
            print("Wizard : You made the right choice, continue in your journey but always stay on the right path. ")

            print("You continue your journey and find two doors, which do you enter?")
            print("1. The one on the right hand side.")
            print("2. The one on the left hand side.")
        else:
            print(f"doing {option2} doesn't help.")
            print("You stumble and die.")

            right = input("> ")

            if right == "1":
                print("Door leads out of the realm back to earth.")
                print("Good job!!!")
                print("You win 🥳🥳😲😲👏👏")
                print("Game over 👏👏👍👍:-)")
            elif right == "2":
                print("You fall into a pit full of scorpions and snakes.")
                print("Always listen to instructions.")
                print("Nice try.")
            else:
                print("Always follow the rules.")



    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. ")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
