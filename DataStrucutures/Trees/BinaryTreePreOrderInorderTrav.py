#Construct Binary Tree From Preorder and Inorder Traversal
#LC 105

"""
    Given preorder and inorder traversal of a tree, construct
    the binary tree

    Note: you may assume duplicates do not exist in the tree
    For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

 """

 #pre-order: visit,left,right
 #in-order:left,visit,right
 #post-order: left,right,visit
 def buildTree(preorder,inorder):
     #couldnt get on first try, come back to
