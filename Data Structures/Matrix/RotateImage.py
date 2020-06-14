#Rotate Image
#LC 48

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

#go layer by layer and swap elements, elementwise
#int(n/2) -1 layers
#note, [~i] == [n-1-i] --> bitwise not
#note swaps are done in parallel, not sequentially!
def rotate90(A):
    n = len(A)
    for i in range(int(n/2)):
        for j in range(n-int(n/2)):
             A[i][j], A[~j][i], A[~i][~j], A[j][~i] =  A[~j][i], A[~i][~j], A[j][~i], A[i][j]


#RT : O(n) --> traverse matrix once
#SC : O(1) --> only need length of array, space allocation not dependent on size of array.
