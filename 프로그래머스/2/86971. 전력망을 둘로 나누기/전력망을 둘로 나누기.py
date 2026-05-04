from collections import deque

def solution(n, wires):
    answer = n
    for k in range(n - 1):
        lst = [[] for _ in range(n + 1)]
        for i in range(n - 1):
            if k == i:
                continue
            else:
                s, e = wires[i]
                lst[s].append(e)
                lst[e].append(s)

        queue = deque()
        queue.append(1)
        visited = [False] * (n + 1)
        visited[1] = True
        cnt = 1
        
        while queue:
            temp = queue.popleft()
            for now in lst[temp]:
                if not visited[now]:
                    queue.append(now)
                    visited[now] = True
                    cnt += 1
        answer = min(answer, abs(cnt - (n - cnt)))
        
    return answer