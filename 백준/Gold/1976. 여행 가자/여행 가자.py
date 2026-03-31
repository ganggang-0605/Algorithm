import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

parent = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            union(i, j)
city = list(map(int, input().split()))

for i in range(1, m):
    if find(city[i] - 1) != find(city[0] - 1):
        flag = False
        break
    if i == m - 1:
        flag = True

if flag:
    print("YES")
else:    
    print("NO")