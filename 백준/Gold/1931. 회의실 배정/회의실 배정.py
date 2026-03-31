import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))

cnt = 0
temp = 0
for i in range(n):
    if lst[i][0] >= temp:
        cnt += 1
        temp = lst[i][1]
print(cnt)