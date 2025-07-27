def solution(numbers, k):
    answer = 0
    idx = 0
    round_numbers = numbers * k
    
    for i in range(1, k + 1):
        answer = round_numbers[idx]
        idx += 2

    return answer