import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

m, n = map(int, input().split())
lst = []
queue = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            queue.append((i, j, 1))
    lst.append(temp)

while queue:
    r, c, cnt = queue.popleft()
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 0:
            queue.append((nr, nc, cnt + 1))
            lst[nr][nc] = cnt + 1

flag = False
ans =0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            flag = True
            break
        ans = max(ans, lst[i][j])

if flag:
    print(-1)
else:
    print(ans - 1)