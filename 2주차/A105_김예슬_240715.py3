num = int(input())
line_num = 0
end_num = 0

while end_num < num:
    line_num += 1
    end_num += line_num
step = end_num - num

if line_num % 2 == 0:
  up = line_num - step
  down = step + 1
else:
  up = step + 1
  down = line_num - step

string = str(up) + "/" + str(down)
print(string)