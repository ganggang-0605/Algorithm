import heapq

def solution(N, road, K):
    answer = 0
    dist = [500001] * (N + 1)
    dist[1] = 0
    queue = []
    
    lst = [[] for _ in range(N + 1)]
    for i in range(len(road)):
        s, e, w = road[i]
        lst[s].append((e, w))
        lst[e].append((s, w))

    heapq.heappush(queue, (0, 1))
    while queue:
        tempWeight, temp = heapq.heappop(queue)
        for now, nowWeight in lst[temp]:
            cost = tempWeight + nowWeight
            if dist[now] > cost:
                dist[now] = cost
                heapq.heappush(queue, (cost, now))

    for now in dist:
        if now <= K:
            answer += 1
    return answer