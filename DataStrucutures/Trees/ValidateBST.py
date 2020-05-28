#Vlaidate Binary Search Tree
#LC 98
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

def isValid(root):
    if root is None:
        return True
    def dfsLeft(root,val):
        if root is None:
            return True
        if root.val >= val:
            return False
        left = dfsLeft(root.left,val)
        right = dfsLeft(root.right,val)
        return left and right
    def dfsRight(root,val):
        if root is None:
            return True
        if root.val <= val:
            return False
        left = dfsRight(root.left,val)
        right = dfsRight(root.right,val)
        return left and right
    return dfsLeft(root.left,root.val) and dfsRight(root.right,root.val) and isValid(root.left) and isValid(root.right)

#RT --> O(n) we traverse every node in the tree
#SC --> O(n) we check the left and right node on every recursive call so store the left and right in recursive stack
