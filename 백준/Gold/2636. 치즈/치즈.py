import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

queue = deque()

time = -1
temp = 0

while 1:
    last = temp
    temp = 0
    queue.append((0, 0))
    time += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = True
                if lst[nr][nc] == 0:
                    queue.append((nr, nc))
                else:
                    lst[nr][nc] = 0
                    temp += 1
    if temp == 0:
        break

print(time)
print(last)
