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
        def buildTree2(preorder,inorder):
            if not inorder:
                return None
            rootIndex = inorder.index(preorder.pop(0))
            root  = TreeNode(inorder[rootIndex])
            root.left = buildTree2(preorder, inorder[:rootIndex])
            root.right = buildTree2(preorder, inorder[rootIndex+1:])
            return root
        return buildTree2(preorder,inorder)

#RT --> O(n) visit all nodes in tree
#SC: O(n) --> store left and right child of each node on recursive stack
