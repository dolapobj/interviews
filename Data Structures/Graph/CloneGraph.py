#Clone Graph
#LC 133

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed).
 For example, the first node with val = 1, the second node with val = 2, and so on.
  The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph.
 Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    visited = {}
    def dfs(node):
        if not node:
            return
        nodeCopy = Node(node.val,list())
        visited[node] = nodeCopy
        for neighbor in node.neighbors:
            if neighbor in visited:
                nodeCopy.neighbors.append(visited[neighbor])
            else:
                nodeCopy.neighbors.append(dfs(neighbor))
        return nodeCopy
    return dfs(node)

#RT : O(n) --> Visit every node
#SC : O(n) --> store each node and neighbors.
