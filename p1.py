s = input()
a = len(s)

if a >= 4:
    print(s[0:2] + s[(a-2):a])

else:
    print("NONE")