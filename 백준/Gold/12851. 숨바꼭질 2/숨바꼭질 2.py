import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, k = map(int, input().split())

queue = PriorityQueue()
queue.put((0, k))

visited = [-1] * 100001
visited[k] = 0

min_time = float('inf')
ans = 0

while queue.qsize() > 0:
    cnt, temp = queue.get()
    if temp == n:
        if min_time == float('inf'):
            min_time = cnt
            ans = 1
        elif min_time == cnt:
            ans += 1
        continue
    if cnt >= min_time:
        continue
        
    if temp - 1 >= 0:
        if visited[temp - 1] == -1 or visited[temp - 1] == cnt + 1:
            visited[temp - 1] = cnt + 1
            queue.put((cnt + 1, temp - 1)) 
    if temp + 1 <= 100000:
        if visited[temp + 1] == -1 or visited[temp + 1] == cnt + 1:
            visited[temp + 1] = cnt + 1
            queue.put((cnt + 1, temp + 1))       
    if temp % 2 == 0:
        if visited[temp // 2] == -1 or visited[temp // 2] == cnt + 1:
            visited[temp // 2] = cnt + 1
            queue.put((cnt + 1, temp // 2))

print(min_time)
print(ans)