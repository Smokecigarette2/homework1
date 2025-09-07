def selection_sort(nums):

    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]

    return nums

print(selection_sort([4,5,6,3,8]))