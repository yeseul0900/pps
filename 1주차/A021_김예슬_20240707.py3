import sys

m_num = int(sys.stdin.readline())
multi_num = 0
for i in range(m_num):
  if i == 0:
    multi_num = int(sys.stdin.readline())
  else:
    multi_num += int(sys.stdin.readline()) - 1
print(multi_num)