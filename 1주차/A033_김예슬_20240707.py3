max_score = 0
rank = 0
for i in range(5):
  score_list = list(map(int, input().split()))
  sum_score = sum(score_list)
  if sum_score > max_score:
    max_score = sum_score
    rank = i+1
print(rank, max_score)