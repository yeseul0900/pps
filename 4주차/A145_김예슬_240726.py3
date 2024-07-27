def solution(price, money, count):
    price_list = []
    for i in range(count):
        price_list.append(price*(i+1))
    sum_price = sum(price_list)
    if sum_price > money:
        answer = sum_price - money
    else:
        answer = 0

    return answer