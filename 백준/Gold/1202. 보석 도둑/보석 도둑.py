import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []

for _ in range(n):
    m, v = map(int, input().split())
    jewel.append((m, v))
jewel.sort()

bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()

ans = 0
candidateJewel = []
idx = 0
for c in bag:
    while idx < n and jewel[idx][0] <= c:
        heapq.heappush(candidateJewel, -jewel[idx][1])
        idx += 1

    if candidateJewel:
        ans -= heapq.heappop(candidateJewel)

print(ans)