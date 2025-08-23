class filt():
    def __init__(self, numbers):
        self.numbers = numbers

    def find_prime(self, x ):
        if x < 2:
            return False
        else:
            for i in range(2, int(x**0.5) + 1):
                if x % i != 0:
                    return True
            return False

    def lamb(self):
        return list(filter(lambda x : self.find_prime(x), self.numbers))


f1 = filt([1,3,4,5,6,7,8,9,10,11,13])
print(f1.lamb())