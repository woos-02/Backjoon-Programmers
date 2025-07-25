def solution(before, after):
    a, b = [], []
    for i in before:
        b.append(i)
    for j in after:
        a.append(j)
    a.sort()
    b.sort()
    for k in range(len(before)):
        if b[k] != a[k]:
            return 0
        
    return 1