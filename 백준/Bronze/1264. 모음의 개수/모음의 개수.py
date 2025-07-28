while True:
    n = input()
    if n == '#':
        break
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            count += 1
    print(count)