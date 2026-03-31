import sys
from collections import deque
input = sys.stdin.readline

dr = [2, 2, 1, -1, -2, -2, -1, 1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

T = int(input())
for _ in range(T):
    l = int(input())
    lst = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    queue = deque()
    queue.append((startX, startY, 0))
    visited[startX][startY] = True
    while queue:
        r, c, cnt = queue.popleft()

        if r == endX and c == endY:
            print(cnt)
            break

        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc]:
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
