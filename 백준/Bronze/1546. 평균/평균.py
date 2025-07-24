n = int(input())
a = list(map(int, input().split()))
max = max(a)

sum = 0
for i in range(0, n):
    a[i] = a[i]/max * 100
    sum += a[i]

total = sum/n
    
print(total)