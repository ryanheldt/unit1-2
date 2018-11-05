import math

name = input()

shape = input("What shape would you like? Availible: Cube or Cylinder:")

if shape == "Cube" or shape == "cube":
    l = int(input("What length do you want? (In feet):"))
    w = int(input("What width do you want? (In feet):"))
    h = int(input("What height do you want? (In feet):"))
    
    vol = l * w * h
    
    volWgals = vol / 7.5
    
    print("The amount of liquid you would put in the cube would be:" + str(volWgals))

elif shape == "Cylinder" or shape == "cylinder":
    r = int(input("What radius do you want? (In feet):"))
    h = int(input("What height do you want? (In feet):"))
    
    vol = (math.pi) * (r ** 2) * h
    
    volWgals = vol / 5.875
    
    print("The amount of liquid you would put in the cylinder would be:" + str(volWgals))
    
else:
    print("That ain't a shape cheif. Please restart")