i = 0
numbers = []
six = 6
plus =  1
def function(i):
    while i < six:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + plus
        print("Number now:", numbers)
        print(f"At the bottom i is {i}")

function(i)
print("The numbers: ")

for num in numbers:
    print(num)

for i in range(0,6) :
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + plus
    print("Number now:", numbers)
    print(f"At the bottom i is {i}")
