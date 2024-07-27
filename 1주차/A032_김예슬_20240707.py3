T = int(input())
T_list = []
for _ in range(T):
  k = int(input())
  n = int(input())
  f0 = [x for x in range(1, n+1)]
  
  for _ in range(k):
    for s in range(1,n):
      f0[s] += f0[s-1]
      
  T_list.append(f0[-1])
  
for i in T_list:
  print(i)