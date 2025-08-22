
def number_of_permut(s):
    res = 1
    for i in range(1,len(s)+1):
        res *= i
    return res

def permut(s):
    if len(s) == 0:
        return "Give me text"
    elif len(s) == 1:
        return [s]
    result = []
    for i in range(len(s)):
        fixed_position = s[i]
        rest = s[:i] + s[i+1:]
        for p in permut(rest):
            result.append(fixed_position + p)

    return result
s = input("Text: ")
print(permut(s), number_of_permut(s))