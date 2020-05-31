#Kth Smallest Element in BST
#LC 230

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.



Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""

#basic idea --> post-order traversal into list and return element at index k-1
#is there a better way though?
#yes! using a stack --> if we continue adding root.left we are always getting smaller.
#when k = 0, we are at the kth smallest element.
def kthSmallest(root,k):
    if root == None:
        return
    inOrder = []
    def dfs(root):
        if root == None:
            return
        dfs(root.left)
        inOrder.append(root.val)
        dfs(root.right)
    dfs(root)
    return inOrder[k-1]

#RT --> O(n) in worst case we visit all nodes in the tree
#SC --> O(n) we store left and right child of node on recursive stack
