def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in my_string:
        if letter not in vowels:
            answer += letter
    return answer