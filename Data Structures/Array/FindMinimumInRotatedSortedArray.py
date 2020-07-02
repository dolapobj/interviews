#FInd Minimum in Rotated Sorted Array
#LC 153
"""
Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

#idea is to perform an altered binary searchm where we determine search direction
#by looking for inflection point, where to the left of inflection point are greater than
# first element in array, and all elements to right are smaller than first element of array
def findMinRotated(nums):
    if len(nums) ==1:
        return nums[0]
    left = 0
    right = len(nums) -1

    if nums[right] > nums[0]:
    ##if array not rotated
        return nums[0]

    while right >= left:
        mid = left + (right-left) //2

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]

        if nums[mid-1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid +1
        else:
            right = mid-1

#RT: O(log(n)) --> we reduce input size by factor of two at each step
#SC: O(1) --> store left and right pointers, independent of input size.
