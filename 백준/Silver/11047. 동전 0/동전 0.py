import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

cnt = 0
for i in range(n - 1, -1, -1):
    temp = k // coin[i]
    k -= temp * coin[i]
    cnt += temp
    if k <= 0: break

print(cnt)
    