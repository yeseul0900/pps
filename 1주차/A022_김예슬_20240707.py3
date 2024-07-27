count = int(input())
time_list = list(map(int, input().split()))
m_list = []
y_list = []

for i in range(count):
  m = 0
  y = 0
  
  y = time_list[i]//30 + 1
  m = time_list[i]//60 + 1
  y_list.append(y)
  m_list.append(m)

M = sum(m_list) * 15
Y = sum(y_list) * 10

if M < Y:
  print("M", M)
elif M > Y:
  print("Y", Y)
else:
  print("Y M", Y)