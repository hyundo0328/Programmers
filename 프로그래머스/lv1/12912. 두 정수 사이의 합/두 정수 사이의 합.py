def solution(a, b):
    # answer = 0
    # if(a <= b):
    #     for i in range(a,b+1):
    #         answer += i
    # else:
    #     for i in range(b,a+1):
    #         answer += i
    # return answer
    
    # range로 범위 지정
    # return sum(range(min(a, b), max(a, b)+1))

    # tuple을 이용한 전환
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))