def solution(price, money, count):
    total = 0
    now = price
    for i in range(count):
        total += price
        price += now
        
    if total > money:
        return total - money
    else:
        return 0