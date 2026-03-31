import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sortedLst = sorted(list(set(lst)))

ans = [bisect_left(sortedLst, i) for i in lst]
print(*ans)
