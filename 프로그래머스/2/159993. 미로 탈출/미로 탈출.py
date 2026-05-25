from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(s, e, maps):
    n, m = len(maps), len(maps[0]) 
    queue = deque([(s[0], s[1], 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[s[0]][s[1]] = True
    
    while queue:
        r, c, cnt = queue.popleft()
        
        if [r, c] == e:
            return cnt
            
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    queue.append((nr, nc, cnt + 1))
                    
    return -1
    
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    visited = [[False for _ in range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = [i, j]
                visited[i][j] = True
            elif maps[i][j] == 'E':
                destination = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
    
    cnt1 = BFS(start, lever, maps)
    cnt2 = BFS(lever, destination, maps)
    if cnt1 == -1 or cnt2 == -1:
        return -1
    else:
        return cnt1 + cnt2