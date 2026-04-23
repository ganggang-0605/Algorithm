import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

one = True
for i in lst:
    if i > 1:
        one = False
        break

result = 0
for i in lst:
    result ^= i

if one:
    if n % 2 == 0:
        print("koosaga")
    else:
        print("cubelover")
else:
    if result == 0:
        print("cubelover")
    else:
        print("koosaga")