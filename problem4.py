

def filter_prime(num):
    result = []
    for i in range(len(num)):
        isprime = True
        if num[i] < 2:
            isprime = False
        else:
            for j in range(2, int(num[i]**0.5) + 1):
                if num[i] % j == 0:
                    isprime = False
                    break
            if isprime:
                result.append(num[i])
    return result


print(filter_prime([1,2,3,4,5,13]))
