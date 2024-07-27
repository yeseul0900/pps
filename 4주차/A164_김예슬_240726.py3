def solution(s):
    answer = [-1] *len(s)
    dic = {}
    
    for i in range(len(s)):
        if s[i] in dic:
            answer[i] = i-dic[s[i]]
        dic[s[i]] = i
    print(dic)
    return answer