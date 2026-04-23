import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = 0
for i in lst:
    result ^= i

win = 0
if result != 0:
    for i in lst:
        if (i ^ result) < i:
            win += 1
print(win)