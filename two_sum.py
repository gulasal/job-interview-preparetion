#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    for i in range(len(nums)):
        first_num = target - nums[i]
        if first_num in nums and nums.index(first_num) != i:
            return [i, nums.index(first_num)]  