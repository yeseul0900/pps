def solution(babbling):
    ong = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for word in ong:
            if word*2 not in i:
                i = i.replace(word," ")
        if i.isspace():
            answer += 1
    return answer