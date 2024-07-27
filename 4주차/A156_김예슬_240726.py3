tree, count = list(map(int, input().split()))
tree_list = list(map(int, input().split()))
end = max(tree_list)
start = 1
while(start <= end):
  mid = (start + end) // 2
  sum = 0
  for i in tree_list:
    temp = i - mid
    if temp > 0:
      sum += temp
  if sum >= count:
    start = mid + 1
  else:
    end = mid - 1

print(end)