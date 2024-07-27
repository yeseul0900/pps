def solution(x):
    num_list = []
    num = list(map(int, str(x)))
    print(num)
    
    if x % sum(num) == 0:
        answer = True
    else:
        answer = False

    return answer