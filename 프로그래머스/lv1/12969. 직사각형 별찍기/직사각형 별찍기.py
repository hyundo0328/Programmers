a, b = map(int, input().strip().split(' '))

# for i in range(0,b):
#     print("*"*a)

answer = ('*'*a +'\n')*b
print(answer)