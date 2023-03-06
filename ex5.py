name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # Ibs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_in_kg = 180 * 0.454 # 1 Ibs = 0.454 kg
height_in_cm = 74 * 2.54 # 1 inch = 2.54 cm
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"That is equal to {height_in_cm} in cm")
print(f"He's {weight} pounds heavy.")
print(f"That is about {weight_in_kg} in kg")

print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f" If I add {age}, {height}, and {weight} I get {total}.")
