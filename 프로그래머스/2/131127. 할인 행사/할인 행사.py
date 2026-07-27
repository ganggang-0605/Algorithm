from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount) - 1):
        if Counter(discount[i:i+10]) == dic:
            answer += 1
            
    return answer
    

        
        
    
    
    
    return answer