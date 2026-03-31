import sys
from collections import deque
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    n, m = map(int ,input().split())
    queue = deque()
    temp = list(map(int, input().split()))
    for i in range(n):
        queue.append((temp[i], i))
    
    cnt = 0
    while queue:
        if queue[0][0] == max(queue)[0]:
            cnt += 1
            if queue.popleft()[1] == m:
                print(cnt)
                break
        else:
            queue.append(queue.popleft())
