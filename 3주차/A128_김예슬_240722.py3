
while(1):
  answer  = "yes"
  check_list = []
  input_str = input()
  if input_str == ".":
    break
  for i in input_str:
    if i in ["[", "("]:
      check_list.append(i)
    elif i == "]":
      if len(check_list) == 0 or check_list[-1] != "[":
        answer = "no"
        break
      else:
        check_list = check_list[:-1]
    elif i == ")":
      if len(check_list) == 0 or check_list[-1] != "(":
        answer = "no"
        break
      else:
        check_list = check_list[:-1]
    else:
      continue
  if len(check_list) != 0:
    answer = "no"
  print(answer)