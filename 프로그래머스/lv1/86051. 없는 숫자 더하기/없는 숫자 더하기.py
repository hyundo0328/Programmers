def solution(numbers):
    
    answer = 0

    for i in range(0,10):
        if(numbers.count(i) == 0):
            answer += i
    
    return answer