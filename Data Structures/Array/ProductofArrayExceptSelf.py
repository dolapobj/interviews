#Product of Array Except Self
#LC 238
"""
Given an array nums of n integers where n > 1,
return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of
the elements of any prefix or suffix of the array
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""


#idea: use the product of all numbers to left and all numbers to the right
def productBesidesSelf(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    for i in range(1,len(nums)):
        left[i] = left[i-1]*nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1]*nums[i+1]
    out = [1]*len(nums)
    for i in range(len(nums)):
        out[i] = left[i]*right[i]
    return out
#RT: O(n) --> Iterate through nums at most three times, regardless of size of input
#SC: O(n) --> allocate three arrays at most. O(3n)-->O(n)
