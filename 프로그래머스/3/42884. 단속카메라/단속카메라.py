def solution(routes):
    routes.sort(key=lambda x: x[1])
    # [-20, -15] [-18, -13] [-14, -5] [-5, -3]
    answer = 0
    
    now = -30001
    for start, end in routes:
        if start > now:
            answer += 1
            now = end
        
    return answer