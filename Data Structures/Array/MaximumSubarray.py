#Maximum Subarray
#LC 53
"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""

#idea --> two options at each step
#         1. add nums[i] to current sum bc nums[i]
#         2. nums[i] is our new start for largest sum subarray
def maximumSubArray(nums):
    currenttMax,currentSum = nums[0],nums[0]
    for i in range(1,len(nums)):
        currentSum += nums[i]
        currentSum = max(currentSum,nums[i])
        currentMax = max(currentSum,currentMax)
    return currentMax

#RT --> O(n)
#SC --> O(1)
