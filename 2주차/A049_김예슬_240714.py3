mo = ["a", "e", "i", "o", "u"]
while(1):
  passwd = input()
  if passwd == "end":
    break
  print_pw = "<" + passwd + ">"
  #모음 확인
  count_mo = 0
  for i in mo:
    if i in passwd:
      count_mo = 1
      break
  if count_mo == 0:
    print(print_pw, "is not acceptable.")
    continue

  #연속 자/모음 확인
  count_s = 0
  count_m = 0
  for i in range(len(passwd)):
    if passwd[i] not in mo:
      count_s += 1
      count_m = 0
      if count_s == 3:
        break
    else:
      count_m += 1
      count_s = 0
      if count_m == 3:
        break
      
  if count_m >2 or count_s>2:
    print(print_pw, "is not acceptable.")
    continue

  #같은 글자가 연속적으로 두개 안오게
  count_same = 0
  for i in range(0, len(passwd)-1):
    
    if passwd[i] == passwd[i+1] and passwd[i] not in ["o", "e"]:
      count_same = 1
      break
  if count_same == 1:
    print(print_pw, "is not acceptable.")
    continue
    
  print(print_pw, "is acceptable.")