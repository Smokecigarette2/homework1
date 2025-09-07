
def bubble_sort(nums):

    for i in range(len(nums)):
        swapped = False
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


print(bubble_sort([4,5,6,2,3,1]))