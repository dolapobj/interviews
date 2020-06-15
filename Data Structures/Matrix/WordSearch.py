#Word Search
#LC 79

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
 The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
#go through board, recursively check if we can find solution at that cell
def exist(board, word):
    if not word:
        return True
    if not board or not board[0]:
        return False
    R,C = len(board),len(board[0])
    for i in range(R):
        for j in range(C):
            if board[i][j] == word[0]:
                if found(board,word,i,j):
                    return True
    return False

def found(board,word,i,j):
    #yay, we have found a match
    if len(word) == :
        return True
    #mark this cell as used
    board[i][j] = None
    for nextPos in [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        #check bounds,  0<= currentRow < R and 0<= currentCol <= C
        if 0 <= nextPos[0] < len(board) and 0 <= nextPos[1] < len(board[0]):
            #backtrack
            if board[nextPos[0]][nextPos[1]] == word[1]:
                if found(board,word[1:],nextPos[0],nextPos[1]):
                    return True
        #rest value in board if we dont find match
        board[i][j] = word[0]
    return False
#RT: O(nm^s) --> O(calls^depth)
#SC : O(n) --> O(n) space for recursive calls on recursive stack
