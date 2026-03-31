import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

m = int(input())
keyList = list(map(int, input().split()))


counter = Counter(lst)
print(' '.join(str(counter[key]) for key in keyList))