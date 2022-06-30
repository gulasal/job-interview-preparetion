"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

"""
nums = [4, 2, 3, 2, 3]
for x in nums:
    if nums.count(x) == 1:
        print(x)
            
