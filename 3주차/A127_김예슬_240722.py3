# input_num = int(input())
# for i in range(input_num):
#   a, b = list(map(int, input().split()))
#   for j in range(max(a, b), (a*b) + 1):
#     if j % a == 0 and j % b == 0:
#       print(j)
#       break

from math import gcd
input_num = int(input())
for i in range(input_num):
  a, b = list(map(int, input().split()))
  print(a*b//gcd(a, b))