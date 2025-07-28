n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
list = [n1, n2, n3, n4, n5]
sum = 0
for i in list:
    if i < 40:
        i = 40
    sum += i
avg = sum // 5
print(avg)