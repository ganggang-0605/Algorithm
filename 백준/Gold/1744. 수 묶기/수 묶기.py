import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
zero = 0
ans = 0

for _ in range(n):
    temp = int(input())
    if temp == 0:
        zero += 1
    elif temp == 1:
        ans += temp
    elif temp > 1:
        plus.append(temp)
    else:
        minus.append(temp)

if plus:
    plus.sort(reverse = True)
for i in range(0, len(plus) - 1, 2):
    ans += plus[i] * plus[i + 1]
if len(plus) % 2 != 0:
    ans += plus.pop()


if minus:
    minus.sort()
if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        ans += minus[i] * minus[i + 1]
else:
    for i in range(0, len(minus) - 1, 2):
        ans += minus[i] * minus[i + 1]
    if zero == 0:
        ans += minus[-1]

print(ans)