import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    lst[i][i] = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    if lst[s-1][e-1] > w:
        lst[s-1][e-1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]

for i in range(n):
    for j in range(n):
        if lst[i][j] == float('inf'):
            lst[i][j] = 0

for i in range(n):
    print(*lst[i])