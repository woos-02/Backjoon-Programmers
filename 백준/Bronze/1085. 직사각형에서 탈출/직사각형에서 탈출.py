x, y, w, h = map(int, input().split())
i = w - x
j = h - y

print(min(x,y,i,j))