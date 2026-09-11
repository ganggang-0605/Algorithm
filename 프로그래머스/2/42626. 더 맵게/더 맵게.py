import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        if scoville[0] >= K: return answer
        
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
        
    if scoville[0] >= K: return answer
    else: return -1