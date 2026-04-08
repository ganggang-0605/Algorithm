import sys
import heapq
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    queue.append(int(input()))

heapq.heapify(queue)
cnt = 0
while len(queue) > 1:
    x, y = heapq.heappop(queue), heapq.heappop(queue)
    cnt += x + y
    heapq.heappush(queue, x + y)

print(cnt)
