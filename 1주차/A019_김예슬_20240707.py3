num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 * num2 * num3
list_count = [0] * 10
for i in str(result):
  list_count[int(i)] += 1
for i in list_count:
  print(i)