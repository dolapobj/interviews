#Subtree of Another tree
#LC 572
"""Given two non-empty binary trees s and t, check whether tree t has exactly the same
structure and node values with a subtree of s. A subtree of s is a tree consists
of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.


Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true
"""

#check if current tree is same, else check left subtree and right subtree
def issubtree(s,t):
    if s == None and t!=None:
        return false
    def issametree(a,b):
        if a == none and b!= none or a!= none and b==none:
            return false
        if a == none and b == none:
            return true
        if a.val != b.val:
            return false

        return isSameTree(a.left,b.left) and isSameTree(a.right,b.right)
    if isSameTree(s,t):
        return True
    return isSubTree(s.left,t) or isSubTree(s.right,t)


#RT --> O(n), we traverse all nodes in tree
#SC --> O(n) we store both left and right children in recursive stack
