def square(num):
    for i in range(num):
        yield(i * i)

for i in square(19):
    print(i)

