def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    l_pos = keypad['*']
    r_pos = keypad['#']
    
    for now in numbers:
        if now in [1, 4, 7]:
            answer += 'L'
            l_pos = keypad[now]
            
        elif now in [3, 6, 9]:
            answer += 'R'
            r_pos = keypad[now]
            
        else:
            now_pos = keypad[now]

            lDistance = abs(now_pos[0] - l_pos[0]) + abs(now_pos[1] - l_pos[1])
            rDistance = abs(now_pos[0] - r_pos[0]) + abs(now_pos[1] - r_pos[1])
            
            if lDistance == rDistance:
                if hand == 'left':
                    answer += 'L'
                    l_pos = now_pos
                else:
                    answer += 'R'
                    r_pos = now_pos
            elif lDistance < rDistance:
                answer += 'L'
                l_pos = now_pos
            else:
                answer += 'R'
                r_pos = now_pos
                
    return answer