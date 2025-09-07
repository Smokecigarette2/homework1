from typing import List

def search_rotat(nums: List[int], target : int) -> int:
    L, R = 0, len(nums) - 1

    while L <= R:
        m = (L+R)//2    #adjust m each iteration
        if nums[m] == target:
            return m

        if nums[L] <= nums[m]:
            if nums[L] <= target < nums[m]:
                R = m - 1
            else:
                L = m + 1
        else:
            if nums[m] <= target < nums[R]:
                L = m + 1
            else:
                R = m - 1

    return -1

print(search_rotat([4,5,6,7,0,1,2], 0))
print(search_rotat([4,5,6,7,0,1,2], 3))
print(search_rotat([1], 1))
print(search_rotat([1], 0))