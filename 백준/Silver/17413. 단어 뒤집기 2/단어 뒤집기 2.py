import sys
import re
input = sys.stdin.readline

s = input().rstrip()

result = ""
word = ""
flag = False

for temp in s:
    if temp == "<":
        result += word[::-1]
        word = ""
        flag = True
        result += temp
    
    elif temp == ">":
        flag = False
        result += temp

    elif flag:
        result += temp
    
    elif temp == " ":
        result += word[::-1] + temp
        word = ""

    else:
        word += temp

result += word[::-1]
print(result)