# user will beable to choose from the radius and diameter
# then from this beable to found the area of said circle

# user to select D for diameter or R for radius
print('If you need to found the diameter or radius')
d_r_input = input('Enter "D" for Diameter or "R" for Radius: ')
if d_r_input == "D":
    diameter_results = int(input("Enter Radius here: "))
    results = diameter_results * 2
    print(results)
elif d_r_input == "R":
    radius_results = int(input("Enter diameter here: "))
    results = radius_results / 2
    print(results)
else:
    print("Besure to use captial D or R")



