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

def maximumSubArray(nums):
    j = 0
    currentMax = float('-inf')
    currentSum = 0
    while j < len(nums):
        currentSum += nums[j]
        if nums[j] > currentSum:
            currentSum = nums[j]
        if currentSum  > currentMax:
            currentMax = currentSum
        j+=1
    return currentMax

#RT --> O(n)
#SC --> O(1)
