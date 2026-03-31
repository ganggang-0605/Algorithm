import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0] 

n, m = map(int, input().split())
lst = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

def BFS(i, j):
    queue = deque()
    count = 0
    queue.append((i, j))
    while queue:
        r, c = queue.popleft()
        count += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if lst[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return count

cnt = 0
max_count = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            max_count = max(max_count, BFS(i, j))
            cnt += 1

print(cnt)
print(max_count)