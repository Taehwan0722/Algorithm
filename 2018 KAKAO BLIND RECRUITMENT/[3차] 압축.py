def solution(msg):
    answer = []
    dic = {chr(ord('A') + i):i + 1 for i in range(26)}
    word = ''
    num = 27
    
    for idx, c in enumerate(msg):
        word += c
        if word not in dic:
            answer.append(dic[word[:-1]])
            dic[word] = num
            word = word[-1]
            num += 1
    
    answer.append(dic[word])
            
    return answer