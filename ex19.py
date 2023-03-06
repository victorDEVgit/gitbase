# creates function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints formatted variable
    print(f"You have {cheese_count} cheeses!")
# prints formatted variable
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# prints string
    print("Man that's enough for a party!")
# prints string with escape sequence
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crakers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crakers)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crakers + 1000)

def no_of_songs(favourite, regular):
    print(f"we have {favourite} songs!")
    print(f"we also have {regular} regular songs!")
    print(f"Wow thats a lot of songs!")
    print(f"Enjoy the songs.\n")

print("number of songs in phone:")
no_of_favourites = 100
no_of_regular = 59
no_of_songs(no_of_favourites, no_of_regular)

print("number of songs on samsung phone")
no_of_songs(123, 456)

print("number of songs on your own phone")
no_of_songs(input(int()), input(int()))

print("number of songs on iphone")
no_of_songs(no_of_favourites + 500, no_of_regular - 10)

print("number of songs on infinix")
no_of_songs(1899-321, 400 +65)

print("number of songs on oppo")
oppo1 = input(int())
oppo2 = input(int())
no_of_songs(oppo1, oppo2)

print("number of songs on huawei")
huawei1 = 123 + no_of_favourites
huawei2 = 456 + no_of_regular
no_of_songs(huawei1, huawei2)

print("number of songs on nokia")
no_of_songs(1000 + huawei1, huawei2 - 10)

print("number of songs on techno")
no_of_songs(oppo1 + oppo2 , huawei1+ huawei2)
