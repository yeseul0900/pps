def solution(N, stages):
    answer = []
    fail_player = [0] * max(stages)
    pass_player = [0] * max(stages)
    ratio_player = {}

    for stage in stages:
        fail_player[stage-1] += 1
        for i in range(stage):
            pass_player[i] += 1
    print(fail_player, pass_player)
    
    for i in range(1, N+1):
        if fail_player[i-1] != 0:
            ratio_player[i] = fail_player[i-1]/pass_player[i-1]
        else:
            ratio_player[i] = 0
    print(ratio_player)
    answer = sorted(ratio_player, key = lambda x: ratio_player[x],reverse=True)
    print(answer)
    return answer