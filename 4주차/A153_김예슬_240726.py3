num = int(input())
time = list(map(int, input().split()))
time = sorted(time)

real_time = []
for i in range(1,num+1):
 real_time.append(sum(time[0:i]))

print(sum(real_time))