def solution(bin1, bin2):
    bn1 = int(bin1, 2)
    bn2 = int(bin2, 2)
    answer = bn1 + bn2
    return str(format(answer, 'b'))