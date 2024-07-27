num = int(input())

def calculate_sol(input_num):
  if input_num == 1:
    return 1
  elif input_num == 2:
    return 2
  elif input_num == 3:
    return 4
  else:
    return calculate_sol(input_num-1) + calculate_sol(input_num-2) + calculate_sol(input_num-3)
for i in range(num):
  input_num = int(input())
  sum = calculate_sol(input_num)
  print(sum)
  