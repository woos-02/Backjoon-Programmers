def solution(sides):
    answer = []
    s1 = sides[0]
    s2 = sides[1]
    if s1 > s2:
        s1 = sides[1]
        s2 = sides[0]
    
    short = s2 - s1
    long = s1 + s2
    for i in range(short + 1, long):
        answer.append(i)
        
    return len(answer)