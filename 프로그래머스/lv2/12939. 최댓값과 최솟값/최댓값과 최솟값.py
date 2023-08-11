def solution(s):
    s = list(map(int,s.split()))
    return str(str(min(s))+" "+str(max(s)))