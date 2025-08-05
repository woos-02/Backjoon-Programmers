# 5줄의 문자열을 입력받아 각 줄을 'words' 리스트에 저장한다.
words = []

# 5줄의 입력을 읽어들임
for i in range(5):
	words.append(input())
    
# 결과를 저장할 빈 문자열 초기화
result = ''

# 입력받은 5줄 중 가장 긴 줄의 길이를 구한다. (모든 가능한 열을 순회하기 위해 필요함.)
max_length = max(len(word) for word in words)

# 각 열을 순서대로 처리하기 위해 최대 길이만큼 반복
for col in range(max_length):
# 각 열마다 5개의 행을 순회하며 문자를 읽음
	for row in range(5):
# 현재 열 인덱스가 현재 행의 문자열 길이보다 작으면, 
		if col < len(words[row]):
# 해당 문자를 결과 문자열에 추가함
			result += words[row][col]
            
print(result)