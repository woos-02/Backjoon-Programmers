def solution(strlist):
    answer = []
    for i in range(0, len(strlist)):
        str_len = len(strlist[i])
        answer.append(str_len)
    return answer