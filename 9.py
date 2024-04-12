def simple_search(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

num = int(input())
for i in range(2, num + 1):
    if simple_search(i):
        print(i)