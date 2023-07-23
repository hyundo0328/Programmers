def solution(n):
    x = 0
    for i in range(1,n+1):
        if(n%i==1):
            x = i
            break
        
    return x