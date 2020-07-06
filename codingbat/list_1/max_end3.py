# Given an array of ints length 3, figure out which is larger, the first or last element in the array,
# and set all the other elements to be that value. Return the changed array.
# max_end3([1, 2, 3]) → [3, 3, 3]

def max_end3(nums):
    result = []
    max_value = max(nums[0], nums[2])
    for i in range(3):
        result.append(max_value)
    return result
