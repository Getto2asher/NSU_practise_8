def sov_vid(x):
    devides = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            devides.append(i)
            devides.append(x // i)
    if sum(devides) == 2 * x:
        return True


sov_nums = []
num_nums = int(input())
for i in range(2, num_nums + 1):
    if sov_vid(i):
        sov_nums.append(i)
print(len(sov_nums))
