import math

def solution(n, stations, w):
    answer = 0
    start = 1
    for station in stations:
        left = station - w
        length = left - start
        answer += math.ceil(length / (2 * w + 1))
        start = station + w + 1
        print(answer)
        
    if start <= n:
        answer += math.ceil((n - start + 1) / (2 * w + 1))
        

    return answer