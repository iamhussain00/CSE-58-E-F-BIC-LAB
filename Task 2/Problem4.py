st = input()
s = input()
for i in range (0,len(s) - len(st)):
    flag = 0
    for j in range(0,len(st)):
       if(st[j] != s[i + j]):
           flag = 1
           break
       
    if(flag == 0):
        print(i,end =" ")
           
