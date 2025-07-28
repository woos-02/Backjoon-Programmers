d = int(input())
cars = map(int, input().split())

count = 0
for i in cars:
    if i == d:
        count += 1

print(count)