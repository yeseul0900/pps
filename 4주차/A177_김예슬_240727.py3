def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    answer = max(height) * max(width)
    return answer