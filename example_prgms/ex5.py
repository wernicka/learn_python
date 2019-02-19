name = 'Zed A. Shaw'
age = 35 # not a lie`
height_in = 74 # inches
weight_lbs = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = height_in * 2.54
weight_kg = weight_lbs * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"That is {height_cm} in centimeters.")
print(f"He weighs {weight_lbs} pounds.")
print(f"That is {weight_kg} in kilograms.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}, depending on the coffee.")

total_us = age + height_in + weight_lbs
print(f"If I add {age}, {height_in}, and {weight_lbs}, I get {total_us}.")

total_metric = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg}, I get {total_metric}.")
