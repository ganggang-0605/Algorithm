def solution(grid):
    u, d, l, r = [-1, 0], [1, 0], [0, -1], [0, 1]
    rails = [
        [],
        [l, r], 
        [u, d],   
        [u, d, l, r], 
        [l, u],        
        [r, u],        
        [r, d],        
        [l, d]        
    ]
    
    n = len(grid)
    m = len(grid[0])
    
    required_tracks = set((i, j) for i in range(n) for j in range(m) if grid[i][j] > 0)
    
    answer = 0
    
    def dfs(now_r, now_c, direction, placed):
        nonlocal answer
        
        if now_r == n - 1 and now_c == m - 1:
            coming = [-direction[0], -direction[1]]
            if coming in rails[grid[now_r][now_c]]:
                if required_tracks.issubset(placed.keys()):
                    valid = True
                    for rr, cc in required_tracks:
                        if grid[rr][cc] == 3 and placed.get((rr, cc)) != 'visited_2':
                            valid = False
                            break
                    if valid:
                        answer += 1
            return
        
        nr, nc = now_r + direction[0], now_c + direction[1]
        
        if 0 <= nr < n and 0 <= nc < m:
            if grid[nr][nc] == -1:
                return
                
            coming = [-direction[0], -direction[1]]
            
            if (nr, nc) in placed or grid[nr][nc] > 0:
                if (nr, nc) in placed and grid[nr][nc] == 0:
                    current_track = placed[(nr, nc)]
                    if current_track == 1 and coming in (u, d):
                        placed[(nr, nc)] = 3
                        dfs(nr, nc, direction, placed)
                        placed[(nr, nc)] = 1
                    elif current_track == 2 and coming in (l, r):
                        placed[(nr, nc)] = 3
                        dfs(nr, nc, direction, placed)
                        placed[(nr, nc)] = 2
                    return
                
                if grid[nr][nc] == 3:
                    visit_state = placed.get((nr, nc), 0)
                    if visit_state == 0 and coming in rails[3]:
                        placed[(nr, nc)] = 'visited_1'
                        dfs(nr, nc, direction, placed)
                        del placed[(nr, nc)]
                    elif visit_state == 'visited_1' and coming in rails[3]:
                        placed[(nr, nc)] = 'visited_2'
                        dfs(nr, nc, direction, placed)
                        placed[(nr, nc)] = 'visited_1'
                    return
                
                if (nr, nc) not in placed:
                    if coming in rails[grid[nr][nc]]:
                        next_dir = [x for x in rails[grid[nr][nc]] if x != coming][0]
                        placed[(nr, nc)] = grid[nr][nc]
                        dfs(nr, nc, next_dir, placed)
                        del placed[(nr, nc)]
                    return
            else:
                for track_num in [1, 2, 4, 5, 6, 7]:
                    if coming in rails[track_num]:
                        next_dir = [x for x in rails[track_num] if x != coming][0]
                        placed[(nr, nc)] = track_num
                        dfs(nr, nc, next_dir, placed)
                        del placed[(nr, nc)]

    dfs(0, 0, r, {(0, 0): grid[0][0]})
    
    return answer