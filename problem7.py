def check(l):
    for i in range(len(l)-1):
        if l[i] == 3 and  l[i+1] == 3:
            return True
        else:
            return False

print(check([1,2,3,3,4]))