s = input()
a = input()
k = int(input())

for i in range(len(a) - len(s)):
    cnt = 0
    for j in range(len(s)):
        if(s[j] != a[i + j]):
            cnt += 1
            
    if(cnt <= k):
        print(i, end = " ")
