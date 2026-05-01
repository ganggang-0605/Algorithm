def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num * 3, reverse=True)
    
    answer = ''.join(numbers_str)
    
    if answer[0] == '0':
        return '0'    
    return answer