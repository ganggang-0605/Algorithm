def solution(s):
    stack = []

    for par in s:
        if par == '(':
            stack.append(par)
        else:
            if stack:
                temp = stack.pop()
                if temp != '(': return False
            else:
                return False
    
    if stack: return False
    else: return True