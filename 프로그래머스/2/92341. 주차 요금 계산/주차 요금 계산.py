import math

def makeMinutes(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    
    in_dict = {}
    final_dict = {}
    
    for record in records:
        time, car, status = record.split()
        minutes = makeMinutes(time)
        
        if car not in final_dict:
            final_dict[car] = 0
            
        if status == "IN":
            in_dict[car] = minutes
        else:
            final_dict[car] += (minutes - in_dict[car])
            del in_dict[car]
        
        
    END = 23 * 60 + 59
    for car, in_minutes in in_dict.items():
        final_dict[car] += (END - in_minutes)
        
    defaultTime, defaultFee, unitTime, unitFee = fees
    
    for car, time in sorted(final_dict.items()):
        fee = 0
        
        if time <= defaultTime:
            fee = defaultFee
        else:
            time -= defaultTime
            fee += (defaultFee + math.ceil(time / unitTime) * unitFee)
            
        answer.append(fee)    
        
    return answer

    