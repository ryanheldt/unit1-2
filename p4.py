import random

num = random.randint(1,9)

gamer = True

while gamer:
    a = int(input("What num you pick b? (1 - 9) "))
    if num == a:
        print("That's it chief")
        gamer = False

    else:
        print("That ain't it chief")
        
print("GOT THAT BREAD")