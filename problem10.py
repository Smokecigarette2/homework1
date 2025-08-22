def unique_list(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1,2,3,3,4,4,5]))