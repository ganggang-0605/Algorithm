from collections import deque

def BFS(v, lst, n):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    cnt = 0
    
    while queue:
        temp = queue.popleft()
        for now in lst[temp]:
            if not visited[now]:
                queue.append(now)
                visited[now] = True
                cnt += 1
    return cnt
    

def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)
    
    answer = 0
    for now in range(1, n + 1):
        cnt1, cnt2 = BFS(now, win, n), BFS(now, lose, n)
        if cnt1 + cnt2 == n - 1:
            answer += 1
    
    return answer