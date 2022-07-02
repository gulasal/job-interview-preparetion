#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

nums = [1,3,5,6]
target = 5
def searchInsert( nums, target: int) -> int:
        for num in nums:
            if (target == 0):
                return 0
            if (num==target):
                return(nums.index(num)) 
            if ((num != target) and (num == (target-1))):
                return(nums.index(num) + 1)
            if ((num != target) and (num ==(target + 1))):
                nums.insert(0, 0)
                return(nums.index(num)-1)