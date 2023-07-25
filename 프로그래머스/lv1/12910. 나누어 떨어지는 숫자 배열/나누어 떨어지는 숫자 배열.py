def solution(arr, divisor):
    
    a = [i for i in arr if i%divisor==0]
    a.sort(reverse=False)
    
    if(len(a)==0):
        return [-1]
    else:
        return a