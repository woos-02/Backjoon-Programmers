def solution(balls, share):
    if share == 0 or balls == share:
        return 1

    answer = 1
    for i in range(1, share + 1):
        answer *= balls - i + 1
        answer //= i
    return answer
