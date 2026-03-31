import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []

for r in range(n):
    for c in range(m):
        if lst[r][c] == 0:
            empty.append((r, c))
        elif lst[r][c] == 2:
            virus.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_safe = 0

for walls in combinations(empty, 3):
    temp_lst = [row[:] for row in lst]
    
    for r, c in walls:
        temp_lst[r][c] = 1
        
    q = deque(virus)
    safe_cnt = len(empty) - 3
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and temp_lst[nr][nc] == 0:
                temp_lst[nr][nc] = 2
                q.append((nr, nc))
                safe_cnt -= 1
                
    if safe_cnt > max_safe:
        max_safe = safe_cnt

print(max_safe)