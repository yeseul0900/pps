num_line = int(input())
num_list = list(map(int, input().split()))
num_list.remove(max(num_list))

print(sum(num_list))
