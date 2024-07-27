num_line = int(input())
line = []
result = []
for _ in range(num_line):
  line.append(int(input()))
line = sorted(line)
count = num_line
for i in range(num_line):
  result.append(line[i] * count)
  count -= 1
print(max(result))