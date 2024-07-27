input_char = input()
string = ""
count = 1
for i in input_char:
  if count % 10 == 0 and count != 0:
    string = string + i
    print(string)
    string = ""
  else:
    string = string + i
  count +=1
print(string)