def solution(s1, s2):
    count = 0
    
    if len(s1) > len(s2):
        for i in s1:
            if i in s2:
                count += 1
        return count
    else:
        for i in s2:
            if i in s1:
                count += 1
        return count