def solution(quiz):
    answer = []
    for i in quiz:
        result = ''
        for j in i.split():
            if j == '=':
                j = '=='
                result += j
            else:
                result += j
        result = eval(result)
        if result == True:
            answer.append("O")
        else:
            answer.append("X")
    return answer