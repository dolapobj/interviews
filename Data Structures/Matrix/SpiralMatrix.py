#Spiral Matrix
#LC 54

"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


#we have four different directions to travel, right, down, left, up
#after we travel in a direction, we ignore that row or column for the future

def printSpiral(matrix):
    R = len(matrix) #rows
    C = len(matrix[0]) #columns

    #now we establish our directions
    top = 0
    bottom = R-1
    left  = 0
    right = C-1
    #directions,
    # 0 --> right
    # 1 --> down
    # 2 --> left
    # 3 --> up
    dir = 0;
    out = []
    #conditions for spiral to exist!
    while (top <= bottom and left <= right):
        #traverse right
        if dir == 0:
            for i in xrange(left,right +1):
                out.append(matrix[top][i])
                #once we print all elements in row, top should increment by 1!
            top +=1
            dir = 1

        #traverse down
        elif dir == 1:
            for i in xrange(top,bottom +1):
                out.append(matrix[i][right])
            right -=1
            dir = 2

        #traverse left
        elif dir == 2:
            for i in xrange(right,left -1,-1):
                out.append(matrix[bottom][i])
            bottom -=1
            dir =  3

        #traverse up!
        elif dir == 3:
            for i in xrange(bottom,top -1,-1):
                out.append(matrix[i][left])
            left +=1
            dir = 0
    return out

#RT : O(n) --> traverse entire array
#SC : O(n) --> mantain a list of elements in matrix 
