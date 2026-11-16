def solution(message, spoiler_ranges):
    answer = 0
    
    newMessage = message.split()
    newMessageIndex = []
    
    idx = 0
    for word in newMessage:
        start_idx = message.find(word, idx)
        end_idx = start_idx + len(word) - 1
        newMessageIndex.append((start_idx, end_idx))
        idx = end_idx + 1
        
    blockSpoiler = []
    
    for s, e in spoiler_ranges:
        i = 0
        
        while i < len(newMessageIndex):
            ms, me = newMessageIndex[i]
            
            if ms <= e and me >= s:
                if newMessage[i] != '*':
                    blockSpoiler.append(newMessage[i])
                    newMessage[i] = '*'

            elif ms > e:
                break
            
            i += 1
                    
    for block in set(blockSpoiler):
        if block not in newMessage:
            answer += 1
    
    return answer