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
    
    
    target = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[target], nums[i] = nums[i], nums[target]  # Partitioning the array
            target += 1
    return nums  



            

    

print(moveZeroes([0,1,0,3,12]))
    