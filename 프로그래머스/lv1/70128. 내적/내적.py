def solution(a, b):
#     answer = 0

#     for i in range(0,len(a)):
#         answer += a[i]*b[i]
        
    # zip을 이용한 배열 불러오기
    return sum([x*y for x, y in zip(a,b)])