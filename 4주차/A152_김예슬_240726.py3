num = int(input())
score_list = []
score_list.append(0)
for _ in range(num):
  score_list.append(int(input()))
score_list.append(0)
dp = [0] * (num + 2)
dp[1] = score_list[1]
dp[2] = score_list[1] + score_list[2]

for i in range(3, num+1):
  dp[i] = max(dp[i-2] , dp[i-3] + score_list[i-1])+ score_list[i]

print(dp[num])