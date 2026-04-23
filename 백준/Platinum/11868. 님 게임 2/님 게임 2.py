import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = 0
for i in lst:
    result ^= i

if result == 0:
    print("cubelover")
else:
    print("koosaga")