import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))
lst.sort()

ex = round(sum(lst) / n)

mid = lst[n//2]

count_dict = Counter(lst)
max_freq = max(count_dict.values())
modes = []
for num, freq in count_dict.items():
    if freq == max_freq:
        modes.append(num)

modes.sort()
mode = modes[1] if len(modes) > 1 else modes[0]

range = lst[-1] - lst[0]

print(ex)
print(mid)
print(mode)
print(range)
