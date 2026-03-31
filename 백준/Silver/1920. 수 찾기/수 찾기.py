import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
keyList = list(map(int, input().split()))
def binarySearch(key, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    
    if lst[mid] == key:
        return 1
    elif lst[mid] > key:
        return binarySearch(key, start, mid - 1)
    else:
        return binarySearch(key, mid + 1, end)
    
for key in keyList:
    print(binarySearch(key, 0, n - 1))