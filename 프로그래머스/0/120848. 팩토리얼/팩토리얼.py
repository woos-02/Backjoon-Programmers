def solution(n):
    base = 1
    m = 1
    while base <= n:
        m += 1
        base *= m
        
    return m - 1