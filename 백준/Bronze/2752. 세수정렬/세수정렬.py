n = map(int, input().split())
list = []
for i in n:
    list.append(i)
list.sort()
print(list[0], list[1], list[2])