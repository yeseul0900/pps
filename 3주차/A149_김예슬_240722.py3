input_num = int(input())
all_list = []
for i in range(input_num):
  body_list = list(map(int, input().split()))
  all_list.append(body_list)

for i in all_list:
  rank = 1
  for j in all_list:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  print(rank, end=" ")