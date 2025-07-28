def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    width = max(x) - min(x)
    height = max(y) - min(y)
    
    return width * height