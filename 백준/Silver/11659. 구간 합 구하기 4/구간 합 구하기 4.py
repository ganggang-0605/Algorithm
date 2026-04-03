import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

prefix = [lst[0]]
for i in range(1, n):
    prefix.append(prefix[i-1] + lst[i])

for _ in range(m):
    s, e = map(int, input().split())
    if s == 1:
        print(prefix[e-1])
    else:
        print(prefix[e-1] - prefix[s-2])
        