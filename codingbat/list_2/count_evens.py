#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


def count_evens(nums):
    return sum(1 for i in nums if i % 2 == 0)
