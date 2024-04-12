salary = []
a = -1
cnt = 0
while a != 0:
    a = int(input())
    if a != 0:
        cnt += 1
        salary.append(a)
print(sum(salary) / cnt)
