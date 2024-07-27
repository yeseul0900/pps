def solution(s):
    answer = True
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] not in num_list:
                answer = False
                break
    else:
        answer = False
    return answer