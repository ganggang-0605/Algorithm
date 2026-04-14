import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(input().rstrip())


ans = 64
for i in range(m - 7):
    for j in range(n - 7):
        cnt = 0

        for c in range(i, i + 8):
            for r in range(j, j + 8):
                if (r + c) % 2 == 0:
                    if lst[r][c] != 'W':
                        cnt += 1
                else:
                    if lst[r][c] != 'B':
                        cnt += 1

        ans = min(ans, cnt, 64 - cnt)

print(ans)