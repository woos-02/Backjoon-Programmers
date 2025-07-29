n = input()
count = 0
for i in range(len(n)//2):
    if n[i] == n[-i-1]:
        count += 1
    else:
        continue

if len(n) // 2 == count:
    print(1)
else:
    print(0)