from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque([(0, 0, 1)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    answer = n * m
    flag = False
    while queue:
        r, c, cnt = queue.popleft()
        
        if r == n - 1 and c == m - 1:
            answer = min(answer, cnt)
            flag = True
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
        
    return answer if flag else -1