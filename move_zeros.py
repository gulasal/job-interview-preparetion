"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

ex: Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

"""
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start_num = 0
    end_num = len(nums) - 1
    count = 0
    
    while (start_num <= end_num):
        if nums[start_num] != 0:
            start_num += 1
        if nums[end_num] != 0:
            
            nums[start_num], nums[end_num] = nums[end_num], nums[start_num]
            start_num += 1
            end_num -= 1
            
        else:
            end_num -= 1
        

            
    return nums

print(moveZeroes([0,1,0,3,12]))
    