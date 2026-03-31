import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for _ in range(r):
    for i in range(min(n, m) // 2):
        temp = lst[i][i]

        for j in range(i, m - 1 - i):
            lst[i][j] = lst[i][j + 1]

        for j in range(i, n - 1 - i):
            lst[j][m - 1 - i] = lst[j + 1][m - 1 - i]

        for j in range(m - 1 - i, i, -1):
            lst[n - 1 - i][j] = lst[n - 1 - i][j - 1]

        for j in range(n - 1 - i, i, -1):
            lst[j][i] = lst[j - 1][i]

        lst[i + 1][i] = temp
                 
for i in range(n):
    print(*lst[i])