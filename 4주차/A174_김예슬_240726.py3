def solution(k, score):
    answer = []
    k_list = []
    for i in score:
        if len(k_list) < k:
            k_list.append(i)
        else:
            if min(k_list) <i:
                k_list.remove(min(k_list))
                k_list.append(i)
        answer.append(min(k_list))
    return answer