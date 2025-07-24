def solution(n, k):
    if n >= 10:
        re = n // 10
        answer = 12000 * n + 2000 * (k - re)
    else:
        answer = 12000 * n + 2000 * k
    return answer