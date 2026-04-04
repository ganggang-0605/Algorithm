import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

start, end = 1, max(lst)
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(k):
        temp += lst[i] // mid

    if temp >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)