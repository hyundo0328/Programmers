import math

def solution(n):
    answer = 0
    
    if(n%math.sqrt(n) == 0.0):
        return int(math.pow(math.sqrt(n)+1,2))
    else:
        return -1