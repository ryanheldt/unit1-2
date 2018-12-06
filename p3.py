s = input()
a = len(s)
b = ''
for i in range(0, a + 1):
    if not i % 2 == 0:
        b += s[i]
    
print(b)