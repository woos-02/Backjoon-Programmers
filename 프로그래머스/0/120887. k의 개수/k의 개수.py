def solution(i, j, k):
    answer = 0
    list = []
    for n in range(i, j+1):
        n = str(n)
        list.append(n[0])
        if len(n) >= 2:
            list.append(n[1])
            if len(n) >= 3:
                list.append(n[2])
                if len(n) >= 4:
                    list.append(n[3])
                    if len(n) >= 5:
                        list.append(n[4])
    for count in list:
        if str(k) in count:
            answer += 1
    return answer 