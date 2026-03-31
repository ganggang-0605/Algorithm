import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int ,input().split())

lst = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = True
    for temp in lst[v]:
        if not visited[temp]:
            DFS(temp)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)