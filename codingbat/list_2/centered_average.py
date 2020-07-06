'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
You may assume that the array is length 3 or more.
'''

def centered_average(nums):
    nums = sorted(nums)
  
    nums.remove(nums[0])
    nums.remove(nums[-1])
  
    count = 0
    result = 0
  
    for i in nums:
        count +=1 
        result = result + i
  
  return result/count
