from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for now in topping:
        left.add(now)
        right[now] -= 1
        if right[now] == 0:
            del(right[now])
        if len(left) == len(right):
            answer += 1
    
    return answer