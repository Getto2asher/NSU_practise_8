def sov_vid(x):
    devides = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            devides.append(i)
            devides.append(x // i)
    if sum(devides) == 2 * x:
        return x


num = int(input())
sov_nums = []
for i in range(2, num + 1):
    if i > num:
        exit()
    else:
        if type(sov_vid(i)) == int:
            sov_nums.append(sov_vid(i))
print(sov_nums)
