def solution(s):
    answer = ''
    count_lst = [0] * 26
    
    for str in s:
        count_lst[ord(str) - 97] += 1
    
    for idx in range(len(count_lst)):
        if count_lst[idx] == 1:
            answer += chr(idx + 97)
    
    return answer