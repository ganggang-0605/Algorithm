import sys
input = sys.stdin.readline

line = input().rstrip()
stack = []
ans = ""

for char in line:
    if char.isalpha():
        ans += char

    elif char == '(':
        stack.append(char)

    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(char)

    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(char)

    elif char == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()

while stack:
    ans += stack.pop()

print(ans)