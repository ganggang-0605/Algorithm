def solution(board, moves):
    n = len(board)
    answer = 0
    stack = []
    for move in moves:
        move -= 1
        for i in range(n):
            if board[i][move] != 0:
                now = board[i][move]
                board[i][move] = 0
                if stack and stack[-1] == now:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(now)
                    
                break
    return answer