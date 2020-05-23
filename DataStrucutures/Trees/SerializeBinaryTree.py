#Serealize and Desearlize a Binary Tree
#LC 297

"""
Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a network
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string
can be deserialized to the original tree structure.

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""
#serialize as level order Traversal using BFS
def serialize(root):
    queue = [root]
    serial  = [root.val if root else None]
    if not root:
        return serial
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            serial.append(node.left.val)
        else:
            serial.append(None)
        if node.right:
            queue.append(node.right)
            serial.append(node.right.val)
        else:
            serial.append(None)
    return str(serial)
"as [1,2,3,null,null,4,5,null,null,null,null]"
def deserialize(serial):
     level = 0

##Could not get first try, again, come back to this problem.
