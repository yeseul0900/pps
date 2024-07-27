num_door = int(input())
first_door = int(input())

if num_door > 5:
  print("Love is open door")
else:
  for i in range(1,num_door):
    if first_door == 0:
      print(i%2)
    else:
      if i%2 == 0: 
        print("1")
      else:
        print("0")