#Invert a Binary Tree
#Leetcode 226

"""
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


Input:
     1
    / \
   2   3

Output:

     1
    / \
   3   2
"""

def invertTree(root):
    if not root:
        return
    if root.left == None and root.right == None:
        return root
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root

#RT: O(n) --> we traverse through every node in the tree
#SC: O(n) --> we store o(h) nodes in the recursive stack,
#             where h is the height of the tree. O(h) --> O(n) because
#             no guarantee it is a BST. 
