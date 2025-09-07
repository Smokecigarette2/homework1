from typing import List
import bisect

def length_LIS(nums: List[int]) -> int:
    tails: List[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

print(length_LIS([4,5,7,9,18]))