n, m = list(map(int, input().split()))
set_price = []
one_price = []

for i in range(m):
  set, one = list(map(int, input().split()))
  set_price.append(set)
  one_price.append(one)

set = min(set_price)
one = min(one_price)

price_list = [(n//6 + 1) * set, one * n, (n//6) * set + one * (n%6)]
  
print(min(price_list))