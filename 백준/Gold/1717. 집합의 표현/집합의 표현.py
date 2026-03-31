import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [i for i in range(n + 1)]
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

for _ in range(m):
    comm, a, b = map(int, input().split())
    if comm == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")