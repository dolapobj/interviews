#Lowest Common Ancestor of BST
#LC 235

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

"""


def lca(root,p,q):
    if root == None:
        return None
    if root.val == p.val or root.val ==q.val:
        return root
    left = lca(root.left,p,q)
    right = lca(root.right,p,q)
    if left and not right:
        return left
    if right and not left:
        return right
    if left and right:
        return root
    return None

#RT: O(n)  --> traverse every node in tree
#SC: O(n) --> we store both left and right child on recursive stack
