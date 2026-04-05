import sys
input = sys.stdin.readline
sys.setrecursionlimit(500)

n = int(input())

num = 1
for i in range(1, n + 1):
    num *= i

num = str(num)
cnt = 0
for i in range(len(num) - 1, 0, -1):
    if num[i] != '0':
        break
    cnt += 1
print(cnt)