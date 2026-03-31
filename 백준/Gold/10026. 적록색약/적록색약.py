import sys
from collections import deque
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n = int(input())
normalVisited = [[False for _ in range(n)] for _ in range(n)]
colorWeakVisited = [[False for _ in range(n)] for _ in range(n)]

normal = []
for _ in range(n):
    normal.append(list(input().rstrip()))
colorWeak = [row[:] for row in normal]

for i in range(n):
    for j in range(n):
        if colorWeak[i][j] == 'R':
            colorWeak[i][j] = 'G'

def BFS(queue, lst, visited, r, c):
    visited[r][c] = True
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if lst[nr][nc] == lst[r][c]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True

normalQueue = deque()
colorWeakQueue = deque()
normalCnt = 1
colorWeakCnt = 1

BFS(normalQueue, normal, normalVisited, 0, 0)
BFS(colorWeakQueue, colorWeak, colorWeakVisited, 0, 0)

normalTemp = normal[0][0]
colorWeakTemp = colorWeak[0][0]
for i in range(n):
    for j in range(n):
        if not normalVisited[i][j]:
            BFS(normalQueue, normal, normalVisited, i, j)
            normalCnt += 1
        if not colorWeakVisited[i][j]:
            BFS(colorWeakQueue, colorWeak, colorWeakVisited, i, j)
            colorWeakCnt += 1

print(normalCnt, colorWeakCnt)