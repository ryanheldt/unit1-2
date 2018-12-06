s = input()
fs = s[0]
flist = []

flist.append(fs)
for i in range(1, len(s)):
    if not fs == s[i]:
        flist.append(s[i])
    if fs == s[i]:
        flist.append('$')
        
a = len(flist)
print(flist[0:a])