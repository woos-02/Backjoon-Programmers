S = input()
i = int(input())

for j in range(0, len(S)):
    if j == i - 1:
        print(S[j])