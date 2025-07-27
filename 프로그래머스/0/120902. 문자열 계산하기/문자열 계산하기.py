def solution(my_string):
    tokens = my_string.split()
    answer = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i + 1])
        
        if op == '+':
            answer += num
        elif op == '-':
            answer -= num
    
    return answer
