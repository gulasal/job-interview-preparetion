#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


def searchInsert(nums, target) -> int:
    start_num = 0
    end_num = len(nums) - 1
    while (start_num <= end_num):
        middle = (start_num + end_num) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start_num = middle + 1
        else:
            end_num = middle -1
    return end_num + 1
print(searchInsert(nums = [1, 2, 3, 4], target = 6))

                