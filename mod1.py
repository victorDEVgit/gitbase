def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice:
        how_much = int(choice)

    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy.")
    else:
        dead("You greedy bastard!")
    print(f"{how_much}")
    

def dead(why):
    print(why, "Good job!")
    exit(0)
