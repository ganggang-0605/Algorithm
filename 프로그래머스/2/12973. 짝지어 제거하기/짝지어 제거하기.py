def solution(s):
    stack = []
    for now in s:
        if stack and stack[-1] == now:
            stack.pop()
        else:
            stack.append(now)
            
    return 1 if not stack else 0