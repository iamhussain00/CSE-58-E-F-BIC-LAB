
st = input()
k = int(input())

count = {}

for i in range(len(st) - k + 1):
    pattern = st[i:i+k]

    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1


max_count = max(count.values())


for pattern in count:
    if count[pattern] == max_count:
        print(pattern, end=" ")
