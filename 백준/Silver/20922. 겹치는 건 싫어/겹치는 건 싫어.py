import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = [0] * 100001
ans = 0
start = 0
for end in range(n):
    cnt[lst[end]] += 1
    while cnt[lst[end]] > k:
        cnt[lst[start]] -= 1
        start += 1

    temp = end - start + 1
    ans = max(temp, ans)

print(ans)