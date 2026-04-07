import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
queue = list(map(int, input().split()))
heapq.heapify(queue)

for _ in range(m):
    x, y = heapq.heappop(queue), heapq.heappop(queue)
    heapq.heappush(queue, x + y)
    heapq.heappush(queue, x + y)    

print(sum(queue))