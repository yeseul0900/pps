count = int(input())
list_num = list(map(int, (input().split())))
v = int(input())
cnt_v = 0
for i in range(count):
    if list_num[i] == v:
        cnt_v += 1
print(cnt_v)