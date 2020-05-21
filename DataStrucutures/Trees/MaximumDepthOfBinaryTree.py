##Maximum Depth of Binary Tree
##Leetcode Problem 104

""" Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. """

 """
    3
   / \
  9  20
    /  \
   15   7

return depth of 3
   """

def maxDepth(root):
    if root == None:
        return 0
    left =  1 + maxDepth(root.left)
    right = 1 + maxDepth(root.right)
    return max(left,right)


#RT analysis: O(n) --> we traverse through all nodes in the tree once in the worst case.
#SC analysis: O(log(n)) --> in the longest path, we store the left and right children to come back to
#                           because we backtrack when we finish traversing the left side.
