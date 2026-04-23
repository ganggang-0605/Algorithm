def solution(number, k):
    stack = []
    for temp in number:
        while k > 0 and stack and stack[-1] < temp:
            stack.pop()
            k -= 1
        stack.append(temp)
        
    if k > 0:
        stack = stack[0:len(stack)-k]

    ans = ''
    for now in stack:
        ans += now
    return ans