#SameTree
#LC Problem 100

""" Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value. """


"""
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false


Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""
#Basic Idea I am thinking: traverse both trees dfs, compare each node at each step
def isSameTree(p,q):
    if p == None and q == None:
        return True
    if p!= None and q == None or p == None and q!=None or p.val != q.val:
        return False
    left =  isSameTree(p.left, q.left)
    right = isSameTree(p.right,q.right)
    return left and right


#RT O(n) --> Traverse through each tree once
#SC O(n) --> we need to store the children for each node, so on the longest path, we store O(h) nodes, or O(n) nodes.
#            not guaranteed a height of log(n) because it is not a BST.
