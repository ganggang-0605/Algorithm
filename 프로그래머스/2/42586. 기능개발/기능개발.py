import math

def solution(progresses, speeds):
    answer = []
    
    days_left = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    current_max_day = days_left[0]
    count = 0
    
    for day in days_left:
        if day <= current_max_day:
            count += 1
        else:
            answer.append(count)
            current_max_day = day
            count = 1
            
    answer.append(count)
    
    return answer