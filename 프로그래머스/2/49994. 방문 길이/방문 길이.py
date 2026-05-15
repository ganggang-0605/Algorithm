move = {'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1]}

def solution(dirs):
    visited = set()
    now = [5, 5]
    answer = 0
    
    for comm in dirs:
        x = now[0] + move[comm][0]
        y = now[1] + move[comm][1]
        
        if 0 <= x < 11 and 0 <= y < 11:
            path = (now[0], now[1], x, y)
            reverse_path = (x, y, now[0], now[1])
            
            if path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer += 1
                
            now = [x, y]
            
    return answer