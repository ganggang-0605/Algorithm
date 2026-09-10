from collections import deque 

def solution(people, limit):
    answer = 0
    
    people.sort()
    queue = deque(people)
    
    while len(queue) > 1:
        light, heavy = queue.popleft(), queue.pop()
        
        if light + heavy > limit:
            queue.appendleft(light)
        answer += 1
        
    if queue:
        answer += 1    
        
    return answer