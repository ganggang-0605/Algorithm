import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    adj[i] = data[1:]

match = [-1] * (m + 1)

def dfs(x):
    for nxt in adj[x]:
        if visited[nxt]: continue
        visited[nxt] = True
        if match[nxt] == -1 or dfs(match[nxt]):
            match[nxt] = x
            return True
    return False

ans = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(i): ans += 1

print(ans)