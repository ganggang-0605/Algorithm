import sys
import heapq
input = sys.stdin.readline

queue = []
for _ in range(int(input())):
    x = int(input())
    if x != 0:
        heapq.heappush(queue, (abs(x), x))
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
