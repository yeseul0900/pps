list_num = [0]*42
for _ in range(10):
  num = int(input())
  list_num[num%42] = 1
print(sum(list_num))