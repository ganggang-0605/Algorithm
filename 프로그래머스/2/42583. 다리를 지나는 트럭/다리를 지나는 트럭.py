from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    fin = 0
    on_bridge = deque()
    current_weight = 0
    while True:
        if idx == len(truck_weights):
            answer += bridge_length
            break
        
        answer += 1
        
        if on_bridge:
            for temp in on_bridge:
                temp[0] += 1
            if on_bridge[0][0] == bridge_length:
                current_weight -= on_bridge.popleft()[1]
                fin += 1
        
        now = truck_weights[idx]
        if current_weight + now <= weight:
            on_bridge.append([0, now])
            current_weight += now
            idx += 1
    
    return answer