from collections import deque

def solution(priorities, location):
    answer = 0
    l = len(priorities)
    queue = deque()
    for i in range(l):
        queue.append((priorities[i], i))
    
    while queue:
        now = queue.popleft()
        if any(now[0] < q[0] for q in queue):
            queue.append(now)
        else:
            answer += 1
            if now[1] == location:
                return answer
        
    return 0