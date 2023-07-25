def solution(x):
      n = x
#     sum = 0

#     while(n != 0):
#         sum += n%10
#         print(sum)
#         n /= 10
#         n = int(n)

#     if(x%sum == 0):
#         return True
#     else:
#         return False

      return n%sum(int(x) for x in str(n)) == 0