#Two Sum
#LC 1
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums,target):
    dict  = dict()
    for i in range(len(nums)):
        if target  - nums[i] in dict:
            return [dict[target - nums[i]],i]
        else:
            dict[nums[i]] = i
