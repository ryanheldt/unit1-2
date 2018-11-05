k = int(input("What day do you want (1-365) "))
a = 4

daysOyear = []
daysOweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(1,366):
    daysOyear.append(i)
    daysOyear.append(daysOweek[a])
    a += 1
    if a == 6:
        a = 0
    

print(daysOyear[k])