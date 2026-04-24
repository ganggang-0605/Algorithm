import sys
import heapq
input = sys.stdin.readline

queue = []
for i in range(int(input())):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, (abs(x), x))