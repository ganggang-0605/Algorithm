def solution(diffs, times, limit):  
    l, r = 1, max(diffs)
    answer = r
    while l <= r:
        mid = (l + r) // 2
        curr = 0
        
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                curr += times[i]
            else:
                cnt = diffs[i] - mid
                curr += (times[i-1] + times[i]) * cnt
                curr += times[i]
        
        if curr <= limit:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer