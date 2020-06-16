#Transpose Matrix
#LC 867

"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""

def transpose(A):
    R,C  = len(A),len(A[0])
    new = []
    for i in range(C):
        row = []
        for j in range(R):
            ##turn columns of A into rows
            row.append(A[j][i])
        new.append(row)
    return new
#RT: O(N)
#SC: O(N) --> cannot be done in place bc of new dimensions is not square matrix! 
