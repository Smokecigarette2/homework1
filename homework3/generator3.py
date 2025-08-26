def divisble(num):
    for i in range(num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in divisble(19):
    print(i)
