"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.


Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def removeElement(nums, val) -> int:
    length = len(nums)
    i = 0
    while length > i:
        if nums[i] == val:
            del nums[i]
            length -= 1
        else:
            i += 1    

    return len(nums), nums
    
    
print(removeElement([3,2,2,3], 3))

