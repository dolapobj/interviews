#Binary Tree Level Order Traversal
#LC #102

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Input:
               3
               / \
              9  20
                /  \
               15   7
Output:

            [
              [3],
              [9,20],
              [15,7]
            ]

"""


def levelOrderTraversal(root):
    ret = []
    dfs(root,0)
    return ret

    def dfs(root,level):
        if root == None:
            return root
        if len(ret) -1 >= level:
            ret[level].append(root.val)
        else:
            ret.append([root.val])
        dfs(root.left,level+1)
        dfs(root.right,level+1)


#RT --> O(n), we traverse through all nodes in the tree.
#SC --> O(n), we backtrack so store  O(h) nodes in recursive stack, but not guaranteed BST, so O(n)
