print("Only 3 Numbers")

a = int(input())
b = int(input())
c = int(input())

list = []
list.append(a)
list.append(b)
list.append(c)

even = 0
odd = 0

for i in range(0, len(list)):
    if list[i] % 2 == 0:
        even += 1
        
    else:
        odd += 1
        
print("evens: " + str(even))
print("odds: " + str(odd))