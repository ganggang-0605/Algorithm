from collections import deque

def solution(n,a,b):
    answer = 0
    queue = deque()
    for i in range(1, n + 1):
        queue.append(i)
    
    while True:
        if len(queue) == 1:
            break
        answer += 1
            
        for i in range(1, n + 1, 2):
            first, second = queue.popleft(), queue.popleft()
            if (a == first and b == second) or (a == second and b == first):
                return answer
                
            if a == first or a == second:
                queue.append(a)
            elif b == first or b == second:
                queue.append(b)
            else:
                queue.append(first)
                
        n //= 2
        
    return answer