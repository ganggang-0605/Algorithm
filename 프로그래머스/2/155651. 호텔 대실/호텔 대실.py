import heapq

def solution(book_time):
    lst = []
    for temp in book_time:
        s = 60 * int(temp[0][:2]) + int(temp[0][3:])
        e = 60 * int(temp[1][:2]) + int(temp[1][3:]) + 10
        lst.append((s, e))
        
    lst.sort(key=lambda x: x[0])
    heap = []
    for s, e in lst:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    
    return len(heap)