def solution(hp):
    jgant = hp // 5
    bjant = hp % 5 // 3
    iant = hp % 5 % 3
    answer = jgant + bjant + iant
    return answer