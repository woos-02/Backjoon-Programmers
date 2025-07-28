s = map(int, input().split())
t = map(int, input().split())

sum_s = sum(s)
sum_t = sum(t)
if sum_s > sum_t :
    print(sum_s)
else:
    print(sum_t)