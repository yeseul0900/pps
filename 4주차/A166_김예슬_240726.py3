def solution(t, p):
    length = len(p)
    num_list = []
    answer = 0
    for i in range(len(t)-length + 1):
        num_list.append(int(t[i:i+length]))
    for i in num_list:
        if i <= int(p):
            answer += 1

    return answer