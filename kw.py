word = "Supplimentary"
print("Lets do stuff to this word")
print (word)
print("\nThis prints all letters before p")
for letters in word:
    if letters == "p":
        break
    print(letters)

print("\nThis removes letter 'p' ")
word = "Supplimentary"
for letters in word:
    if letters == "p":
        continue
    print(letters)

print("\nThis removes all vowels")
word = "Supplimentary"
for letters in word:
    if letters == "a" :
        continue
    if letters == "e":
        continue
    if letters == "i":
        continue
    if letters == "u":
        continue
    print(letters)

print("Lets do some maths !")
print("a = ")
user1 = input("> ")
print("b = ")
user2 = input("> ")
a = int(user1)
b = int(user2)
print("lets divide a by b")
assert a != 0, "Zero Division Error"
print(a/b)

class Food:
    menu1 = 'Appetizers'
    menu2 = 'entree'
    menu3 = 'Dessert'

    def __init__(self, food1, food2):
        self.food1 = food1
        self.food2 = food2

meal1 = Food("Tossed green salad with bread", "First")
meal2 = Food("Sauteed chicken breast on a bed of rice with fresh raddish rosette" ,"Second")
meal3 = Food("Chocholate mousse with raspberry coulis and whipped cream" , "Third")

print("\n\nLets see some classic resturant menu")

print("\nThis is the first meal details :")
print("This meal is a", meal1.menu1)
print("It is a", meal1.food1)
print("It is taken", meal1.food2)

print("\nThis is the second meal details :")
print("This meal is an", meal2.menu2)
print("It is a", meal2.food1)
print("It is taken", meal2.food2)

print("\nThis is the third meal details :")
print("This meal is a", meal3.menu3)
print("It is a", meal3.food1)
print("It is taken", meal3.food2)

list = ['rice', 'beans', 'orroro', 'epo', 'fish', 'garri']
print("\nThis is the list of foodstuff")
print(list)
print("I dont need garri,delete garri")
print("\nDeleting garri .........")
del list[5]
print("Deleted")
print("\nNow lets see the list")
print(list)

list2 =[1,2,3,4,5,6,7,8,9,10]
for num in list2 :
    if num % 2 == 0 :
        print('\n',num)
    elif num % 2 != 0:
        continue
    else:
        break

def divide(x,y):
    try:
        print(f'\n Dividing {x} by {y} ........')
        Result = x/y
    except ZeroDivisionError :
        print('sorry can\'t divide with zero')

    else:
        print('Your answer is', Result)
    finally:
        print('Task completed !!!')

divide(45,5)
divide(78,12)
divide(656,0)
print('\n')
string = 'print("Add 5 to 5 =",5 + 5)'
exec(string)
from math import *
print('\n')
exec('print(dir())')
print('\n')
exec('print(dir())',{})
exec('print(factorial(5))',{"factorial" : factorial})
exec("print(cos(60))",{"cos": cos})
print("\nLets use lambda to do some stuff")
str1 = "Nigeria our country"
print(str1)
print("Lets turn this capital and write it backwards using lambda")
lam1 = lambda string: print(string.upper() [:: -1])
lam1(str1)

print("Lets take a test.\n")
print("\n\nI can hold a car but i can't hold a feather,What am I ? ")
result = True
def last():
    if 9 is 9 or 4 is 4:
        print("9 is 9 or 4 is 4")
    if 9 is not 5 or 9  :
        print("9 is not 5 or 9")
    if 1 + 1 is 2:
       print(" ") 
    
    def last2(a,b):
        yield a + b
    num = last2(5,54)
    print(num)

    from sys import argv
    script , filename = argv
    with open(filename, 'w') as file:
        file.write("Hello World.\nLord I thank you for sunshine\nI thank you for rain\nI thank you for joy\nI thank you for pain.")
    
    def last3():
        j = "junglecruise"
        for i in j:
           print(i)
           yield(i)
      
    last3() 
           
    a = 5
    if a % 2 != 0:
        raise Exception("Number should be even")            

from sys import exit
while True:
    choice = input("> ")
 
    if choice == "brake" and result:
        print("That's so close,try again")
    elif choice == "garage"  and  result :
        print("Wow you got the answer !!!")
        last()
        exit(0)
    else:
        print("Wrong !!!")
