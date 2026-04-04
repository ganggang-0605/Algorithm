import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s, e = map(int, input().split())
    d = e - s
    rt = int(d ** 0.5)
    if d == rt * rt:
        ans = 2 * rt - 1
    elif rt * rt <= d <= rt * rt + rt:
        ans = 2 * rt
    elif d > rt*rt + rt:
        ans = 2 * rt + 1
    print(ans)