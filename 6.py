num = int(input())
space = ' '
star = '*'

for i in range(1, num + 1):
    print(space * (num - i) + star * i)