import sys
input = sys.stdin.readline

n = int(input())
enter = {}
for i in range(n):
    enter[input().rstrip()] = i

out = []
for i in range(n):
    out.append(enter[input().rstrip()])

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if out[i] > out[j]:
            ans += 1
            break

print(ans)