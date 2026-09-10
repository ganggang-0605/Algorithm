from collections import deque

def solution(numbers, target):
    answer = 0
    
    queuePlus, queueMinus = deque(), deque()
    queuePlus.append((numbers[0], 0))
    queueMinus.append((-numbers[0], 0))
    
    while queuePlus:
        now, i = queuePlus.popleft()
        
        if i == len(numbers) - 1 and now == target:
            answer += 1
        
        if i < len(numbers) - 1:
            queuePlus.append((now + numbers[i + 1], i + 1))
            queuePlus.append((now - numbers[i + 1], i + 1))

    while queueMinus:
        now, i = queueMinus.popleft()
        
        if i == len(numbers) - 1 and now == target:
            answer += 1
        
        if i < len(numbers) - 1:
            queueMinus.append((now + numbers[i + 1], i + 1))
            queueMinus.append((now - numbers[i+ 1], i + 1))
    
    return answer