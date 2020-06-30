#Maximum Product Subarray
#LC 152

"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

#idea--> at every step we have three options
#       1. we get a max product by multiplying by current max so far with current element
#       2. we get a max product by multiplying current min so far with current element (multiply negs)
#       3. the current element can be the start for the maximum product subarray
def maxProductSubarray(nums):
    maxProduct,minProduct,ans = nums[0],nums[0],nums[0]
    for i in range(1,len(nums)):
        tempMax = max(nums[i], nums[i]*maxProduct,nums[i]*minProduct)
        tempMin = min(nums[i], nums[i]*maxProduct,nums[i]*minProduct)
        maxProduct,minProduct = tempMax,tempMin
        ans = max(ans,maxProduct)
    return ans

#RT: O(n) --> loop through once
#SC: O(1) --> store 4 variables that are updated in each iteration
