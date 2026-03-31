import sys

k = int(sys.stdin.readline())

size = 1
while size < k:
    size *= 2

print(size, end = ' ')

cnt = 0
temp = size

while k:
    if k % temp == 0:
        break

    temp //= 2
    cnt += 1

print(cnt)