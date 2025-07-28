def solution(keyinput, board):
    answer = []
    lr = 0
    ud = 0
    bd_lr = board[0] // 2
    bd_ud = board[1] // 2
    for i in keyinput:
        if i == "left" and lr > -bd_lr:
            lr -= 1
        elif i == "right" and lr < bd_lr:
            lr += 1
        elif i == "up" and ud < bd_ud:
            ud += 1
        elif i == "down" and ud > -bd_ud:
            ud -= 1
    answer.append(lr)
    answer.append(ud)
    return answer