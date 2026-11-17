def solution(bandage, health, attacks):
    max_health = health
    t, x, y = bandage
    last_time = 0
    
    for a_time, damage in attacks:
        sec = a_time - last_time - 1
        
        if sec > 0:
            heal = (sec * x) + ((sec // t) * y)
            health = min(max_health, health + heal)
        
        health -= damage
        if health <= 0:
            return -1
        
        last_time = a_time
        
    return health