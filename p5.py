a = int(input("How many feet does the snail go up during the day? "))
b = int(input("How many feet does the snail go down during the night? "))
h = int(input("How height does the snail need to go? "))

snailThere = False

hC = 0
day = 0

while not snailThere:
    if a > b:
        h2 = a - b
        hC += h2
        day += 1
        if hC > h:
            print("The snail made it on day " + str(day))
            snailThere = True
        else:
            pass
    
    elif a < b:
        print("The snail will never reach his dreams ;(")
        snailThere = True
        
    else:
        print("You did something wrong cheif. Please reset.")
        snailThere = True