'''
def spy_game(nums):
    cipher = []
    target = "007"
    for i in range(len(nums)-1):
        if nums[i] == 0 or nums[i] == 7:
            cipher.append(nums[i])

            if [target.split()] in cipher:
                return True
    return False

def check_combos(text):
    if len(text) == 1:
        return [text]
    result = []
    for i in range(len(text) - 1):
        fixed_value = text[i]
        rest = text[:i] + text[i+1:]
        for p in check_combos(rest):
            result.append(fixed_value + rest)
    return result'''
from zoneinfo import reset_tzpath


def spy_game(nums):
    goal = [0,0,7]

    for i in range(len(nums)):
        if nums[i] == goal[0]:
            goal.pop(0)
            if len(goal) == 0:
                return True
    return False

print(spy_game([1,2,3,4,5,0,0,7]))

print(spy_game([1,2,4,0,0,7,5]))