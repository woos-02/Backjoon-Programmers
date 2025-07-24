def solution(numbers):
    numbers.sort(reverse=True)
    n1 = numbers[0]
    n2 = numbers[1]
    answer = n1 * n2
    return answer