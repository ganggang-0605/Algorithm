from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def solution(land):
    m = len(land)
    n = len(land[0])
    visited = [[False] * n for _ in range(m)]
    col_sums = [0] * n
    
    for r in range(m):
        for c in range(n):
            if land[r][c] == 1 and not visited[r][c]:
                queue = deque([(r, c)])
                visited[r][c] = True
                size = 0
                cols = set()
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    size += 1
                    cols.add(curr_c)
                    
                    for k in range(4):
                        nr, nc = curr_r + dr[k], curr_c + dc[k]
                        if 0 <= nr < m and 0 <= nc < n:
                            if not visited[nr][nc] and land[nr][nc] == 1:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                
                for col in cols:
                    col_sums[col] += size
                    
    return max(col_sums)