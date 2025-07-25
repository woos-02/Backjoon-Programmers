def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        numbers.pop()
        answer.extend(numbers)
    else:
        re = numbers.pop(0)
        answer.extend(numbers)
        answer.append(re)
        
    return answer