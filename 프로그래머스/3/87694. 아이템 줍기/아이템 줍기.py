from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def draw_border(rectangle):
    board = [[0] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2
                
                elif board[i][j] != 2:
                    board[i][j] = 1
                    
    return board

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    lst = draw_border(rectangle)
    n, m = len(lst), len(lst[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((characterX * 2, characterY * 2, 0))
    visited[characterX * 2][characterY * 2] = True
    while queue:
        r, c, cnt = queue.popleft()
        
        if r == itemX * 2 and c == itemY * 2:
            answer = cnt // 2
            break
            
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
                
    return answer