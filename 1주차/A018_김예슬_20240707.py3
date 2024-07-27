N_num = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

value_S = 0
for i in range(N_num):
  value_S += min(A_list) * max(B_list)
  A_list.remove(min(A_list))
  B_list.remove(max(B_list))

print(value_S)