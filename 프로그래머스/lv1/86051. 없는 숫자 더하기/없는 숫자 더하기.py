def solution(numbers):
    
    answer = 0

    # for i in range(0,10):
    #     if(numbers.count(i) == 0):
    #         answer += i
    
    # for i in range(1,10):
    #     if i not in numbers:
    #         answer += i
    
    # return answer
    
    return sum(range(1,10)) - sum(numbers)