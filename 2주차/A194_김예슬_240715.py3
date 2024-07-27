count = int(input())
for i in range(count):
  list_num = list(map(int, (input().split())))
  print(f"Case #{i+1}: {list_num[0]} + {list_num[1]} = {list_num[0]+list_num[1]}")