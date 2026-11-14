import math

def solution(signals):
    n = len(signals)
    
    cycles = []
    for g, y, r in signals:
        cycles.append(g + y + r)
    
    M = math.lcm(*cycles)
    
    for t in range(1, M + 1):
        isAllYellow = True
        temp = []
        
        for i in range(n):
            g, y, _ = signals[i]
            time = (t - 1) % cycles[i]
            
            if not (g <= time < g + y):
                isAllYellow = False
        
        if isAllYellow: return t
    
    return -1