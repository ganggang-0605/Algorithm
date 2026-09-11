import heapq

def solution(n, edge):
    lst = [[] for _ in range(n + 1)]
    queue = []
    distance = [50000] * (n + 1)
    distance[1] = 0
    visited = [False] * (n + 1)
    visited[1] = True
    
    
    for s, e in edge:
        lst[s].append(e)
        lst[e].append(s)
        
    heapq.heappush(queue, (0, 1))
    
    while queue:
        dist, temp = heapq.heappop(queue)
        
        for now in lst[temp]:
            if not visited[now] and distance[now] > dist + 1:
                distance[now] = dist + 1
                visited[now] = True
                heapq.heappush(queue, (distance[now], now))
                
                
    M = 0
    for i in range(1, len(distance)):  
        if distance[i] > M:
            M = distance[i]
    
    print(distance)
    answer = 0
    for i in range(1, len(distance)):
        if distance[i] == M:
            answer += 1
            
    
    return answer