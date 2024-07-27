input_list = input().split()
list_int = list(map(int, input_list))
sum = 0
for i in range(len(list_int)):
  sum = sum + pow(list_int[i], 2)
valid_value = sum%10
print(valid_value)