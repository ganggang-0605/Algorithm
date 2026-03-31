import sys
input = sys.stdin.readline

line = input().rstrip().split("-")
ans = sum(map(int, line[0].split("+")))

for i in line[1:]:
    ans -= sum(map(int, i.split("+")))

print(ans)