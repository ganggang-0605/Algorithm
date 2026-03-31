import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
lst = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

def BFS(v):
    cnt = 0
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for now in lst[temp]:
            if not visited[now]:
                queue.append(now)
                visited[now] = True
                cnt += 1
    return cnt

print(BFS(1))