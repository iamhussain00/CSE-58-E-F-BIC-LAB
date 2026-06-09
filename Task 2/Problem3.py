
st = input()
s = ""
for i in range (0,len(st)):
    if(st[i] == 'A'):
        s += 'T'
    elif(st[i] == 'C'):
        s += "G"
    elif(st[i] == 'G'):
        s += 'C'
    else:
        s += 'A'
s = s[::-1]

print(s)
