def solution(s):
    p = int(s.count('p')) + int(s.count('P'))
    y = int(s.count('y')) + int(s.count('Y'))

    if(p == y):
        return True
    else:
        return False

    # s.lower().count('p') == s.lower().count('y')
    
    return True