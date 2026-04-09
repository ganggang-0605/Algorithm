import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    temp = map(int, input().split())
    for num in temp:
        if len(lst) < n:
            heapq.heappush(lst, num)
        else:
            if num > lst[0]:
                heapq.heappushpop(lst, num)

print(lst[0])
