def solution(M, N):
    answer = M * N - 1
    if M == 1 and N == 1:
        answer = 0
    return answer