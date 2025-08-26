def evens(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield(i)

n = int(input(": "))
for i in evens(n):
    if i < n - 1:
        print(i, end=",")
    else:
        print(i)
