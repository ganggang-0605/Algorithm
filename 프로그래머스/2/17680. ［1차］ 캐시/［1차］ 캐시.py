from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    for now in cities:
        now = now.lower()
        if not cache or len(cache) < cacheSize:
            if cacheSize != 0:
                if now not in cache:
                    cache.append(now)
                    answer += 5
                else:
                    cache.remove(now)
                    cache.append(now)
                    answer += 1
            else:
                answer += 5
        else:
            if cacheSize != 0:
                if now not in cache:
                    cache.popleft()
                    cache.append(now)
                    answer += 5
                else:
                    cache.remove(now)
                    cache.append(now)       
                    answer += 1
            else:
                answer += 5
    return answer