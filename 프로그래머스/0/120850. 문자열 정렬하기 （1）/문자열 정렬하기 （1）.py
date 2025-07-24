def solution(my_string):
    answer = []
    
    for element in my_string:
        if ord(element) < 65:
            answer.append(int(element))
            
    answer.sort()
    return answer