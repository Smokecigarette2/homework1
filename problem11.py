def check(word):
    for i in range(len(word)//2):
        right = word[len(word) - 1 - i]
        left  = word[i]
        if left != right:
            return False
    return True


print(check("bob"))