import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 1:
                continue
            else:
                if lst[i][k] == 1 and lst[k][j] == 1:
                    lst[i][j] = 1

for i in range(n):
    print(*lst[i])