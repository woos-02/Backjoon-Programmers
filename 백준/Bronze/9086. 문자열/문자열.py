T = int(input())
for i in range(0, T):
    n = input()
    if len(n) == 1:
        print(n[0]*2)
    else:
        print(n[0]+n[-1])