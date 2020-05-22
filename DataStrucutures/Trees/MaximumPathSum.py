#MaximumPathSum
#LC 124

"""Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any
node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""
#Initial Ideas --> This seems like a dp problem, because we need to explore
#                  all options, and continuously take the max of our next decision and
#                  current maximum path.

#Come back to this problem, couldn't solve on first try. 
