def histogram(nums):
    hist = ""
    for i in range(len(nums)):
        hist += nums[i] * "*"
        hist += "\n"
        if i == len(nums) - 1:
            return hist


print(histogram([4,4,4]))