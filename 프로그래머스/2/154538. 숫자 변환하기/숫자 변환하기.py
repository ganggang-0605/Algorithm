import heapq

def solution(x, y, n):
    answer = []
    queue = [[0, x]]
    visited = [False] * (y + 1)
    
    while queue:
        now = heapq.heappop(queue)
        if now[1] > y:
            continue
        
        if not visited[now[1]]:
            visited[now[1]] = True

            if now[1] == y:
                return now[0]

            heapq.heappush(queue, [now[0] + 1, now[1] * 2])        
            heapq.heappush(queue, [now[0] + 1, now[1] * 3])     
            heapq.heappush(queue, [now[0] + 1, now[1] + n])     
    
    return -1
