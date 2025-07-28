h, m, s = map(int, input().split())
need_s = int(input())

total = h * 3600 + m * 60 + s + need_s

h = total // 3600
m = (total - h * 3600) // 60
s = total % 60

if h >= 24:
    h = h % 24
    print(h, m, s)
else:
    print(h, m, s)