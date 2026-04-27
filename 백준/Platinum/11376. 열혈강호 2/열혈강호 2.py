import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    adj[i] = data[1:]

match = [0] * (m + 1)
visited = [0] * (m + 1)
step = 0

def dfs(x):
    for nxt in adj[x]:
        if visited[nxt] == step: 
            continue
            
        visited[nxt] = step
        
        if match[nxt] == 0 or dfs(match[nxt]):
            match[nxt] = x
            return True
    return False

ans = 0
for i in range(1, n + 1):
    for _ in range(2):
        step += 1
        if dfs(i):
            ans += 1

print(ans)