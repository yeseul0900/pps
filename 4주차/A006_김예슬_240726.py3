def solution(s):
    answer = True
    s = s.lower()
    p = 0
    y = 0
    print(s)
    for i in range(len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i]  == 'y':
            y += 1      
    if p != y:
        answer = False

    return answer