def solution(points, routes):
    robot_paths = []
    
    for route in routes:
        r, c = points[route[0] - 1]
        path = [(r, c)]
        
        for i in range(1, len(route)):
            target_r, target_c = points[route[i] - 1]
            
            while r != target_r:
                if r < target_r: 
                    r += 1
                else: 
                    r -= 1
                path.append((r, c))
                
            while c != target_c:
                if c < target_c: 
                    c += 1
                else: 
                    c -= 1
                path.append((r, c))
                
        robot_paths.append(path)
        
    answer = 0
    max_time = max(len(path) for path in robot_paths)
    
    for t in range(max_time):
        pos_count = {}
        
        for path in robot_paths:
            if t < len(path):
                pos = path[t]
                
                if pos in pos_count:
                    pos_count[pos] += 1
                else:
                    pos_count[pos] = 1
                    
        for count in pos_count.values():
            if count >= 2:
                answer += 1
                
    return answer