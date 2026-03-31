import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

def BFS(v):
    queue = deque()
    queue.append((v, 0))
    visited = [5001] * (n + 1)
    visited[v] = 0
    while queue:
        temp, tempCnt = queue.popleft()
        for now in lst[temp]:
            if visited[now] == 5001:
                queue.append((now, tempCnt + 1))
                visited[now] = tempCnt + 1
    return sum(visited[1:])


cntLst = [5001]
for i in range(1, n + 1):
    cntLst.append(BFS(i))

print(cntLst.index(min(cntLst)))

