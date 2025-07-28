def solution(score):
    answer = []
    for e, m in score:
        avg = (e + m) / 2
        answer.append(avg)
    
    answer_sed = sorted(answer)
    answer_sed.reverse()
    
    answer_ind = []
    for j in answer:
        answer_ind.append(answer_sed.index(j)+1)
        
    return answer_ind