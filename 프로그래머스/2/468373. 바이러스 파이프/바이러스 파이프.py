from collections import deque

def solution(n, infection, edges, k):
    adj = {1: [[] for _ in range(n + 1)],
           2: [[] for _ in range(n + 1)],
           3: [[] for _ in range(n + 1)]}
    
    pipe_types = set()
    for u, v, t in edges:
        adj[t][u].append(v)
        adj[t][v].append(u)
        pipe_types.add(t)
        
    start_infected = frozenset([infection])
    queue = deque([(start_infected, -1, 0)])
    
    visited_states = set([(start_infected, -1)])
    
    max_infected_count = 1
    
    while queue:
        curr_infected, prev_pipe, step = queue.popleft()
        
        if len(curr_infected) > max_infected_count:
            max_infected_count = len(curr_infected)
            
        if step == k:
            continue
            
        for p in pipe_types:
            if p == prev_pipe:
                continue
                
            next_infected = set(curr_infected)
            inner_queue = deque(curr_infected)
            
            while inner_queue:
                node = inner_queue.popleft()
                for nxt in adj[p][node]:
                    if nxt not in next_infected:
                        next_infected.add(nxt)
                        inner_queue.append(nxt)
                        
            next_infected_fs = frozenset(next_infected)
            
            state = (next_infected_fs, p)
            if state not in visited_states:
                visited_states.add(state)
                queue.append((next_infected_fs, p, step + 1))
                
    return max_infected_count