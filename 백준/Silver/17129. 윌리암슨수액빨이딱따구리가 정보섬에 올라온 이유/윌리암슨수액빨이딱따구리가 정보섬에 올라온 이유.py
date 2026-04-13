import sys
from collections import deque
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(input().rstrip())
    
queue = deque()
visited = [[False] * m for _ in range(n)]
    
for i in range(n):
    for j in range(m):
        if lst[i][j] == '2':
            queue.append((i, j, 0))
            visited[i][j] = True

while queue:
    r, c, w = queue.popleft()
        
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
            
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            char = lst[nr][nc]
                
            if char == '1':
                continue
                
            if char != '0': 
                print("TAK")
                print(w + 1)
                sys.exit()
                
            visited[nr][nc] = True
            queue.append((nr, nc, w + 1))

print("NIE")