def all_nums(n):
    for i in range(n, 0, -1):
        yield (i)

for i in all_nums(15):
    print(i)