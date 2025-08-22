numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    r = (numlegs - 2*numheads)/2

    c = numheads - r
    return r, c


print(solve(numheads, numlegs))