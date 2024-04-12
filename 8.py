s = '123456789'
k = 1
while k < 10:
    for i in range(1, len(s)+1):
        print(f'{int(s[:i])} * {8} + {k} = {int(s[:i]) * 8 + k}')
        k += 1

l = 2
while l < 11:
    for i in range(1, len(s)+1):
        print(f'{int(s[:i])} * {9} + {l} = {int(s[:i]) * 9 + l}')
        l += 1

for i in range(1, 10):
    a = int('1' * i)
    print(f'{a} * {a} = {a**2}')
