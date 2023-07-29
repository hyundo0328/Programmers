def solution(phone_number):
    answer = phone_number
    
    answer = answer.replace(answer[:len(answer)-4],'*'*(len(answer)-4))
    
    return answer