room_number =  input()
number_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(room_number)):
  temp = int(room_number[i])
  if temp == 6 or temp == 9:
    if number_list[6] <= number_list[9]:
      number_list[6] += 1
    else:
      number_list[9] += 1

  else:
    number_list[temp] += 1

set_num = max(number_list)
print(set_num)