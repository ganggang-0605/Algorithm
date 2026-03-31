import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1 ,1]
dc = [-1, 1, 0, 0]

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
lst = []
for _ in range(n):
    lst.append(list(input().rstrip()))

queue = deque()
queue.append((0, 0, 1))
visited[0][0] = True
while queue:
    r, c, cnt = queue.popleft()
    if r == n - 1 and c == m - 1:
        print(cnt)
        break
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] != '0' and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc, cnt + 1))
