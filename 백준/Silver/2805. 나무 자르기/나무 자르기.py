import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

left, right = 0, max(heights)
result = 0

while left <= right:
    mid = (left + right) // 2
    
    total_wood = 0
    for h in heights:
        if h > mid:
            total_wood += h - mid
            
    if total_wood >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)