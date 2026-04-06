import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    lst = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        lst[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                cnt += 1
                while queue:
                    r, c = queue.popleft()
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                            if lst[nr][nc] == 1:
                                queue.append((nr, nc))
                                visited[nr][nc] = True

    print(cnt)