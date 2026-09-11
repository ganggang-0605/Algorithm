from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False] * (len(computers))
    
    for i in range(len(computers)):
        if not visited[i]:
            answer += 1
            visited[i] = True
            queue.append(i)
            
            while queue:
                temp = queue.popleft()
                for now in range(len(computers)):
                    if computers[temp][now] == 1 and not visited[now]:
                        queue.append(now)
                        visited[now] = True

    return answer