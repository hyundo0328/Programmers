def solution(s):
    s = s.split(" ")

    for i in range(len(s)):
        # capitalize는 문장의 첫문자만 대문자로 자동으로 바꿔주는 메소드이다.
        s[i] = s[i].capitalize()

    answer = ' '.join(s)
    
    return answer