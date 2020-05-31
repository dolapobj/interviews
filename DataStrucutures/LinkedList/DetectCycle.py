#Determine whether a linked list contains a cycle
#LC 141

"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail
connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


"""

def hasCycle(head):
    if head  == None or head.next == None:
        return False
    slow = head
    fast = head.next
    while slow!= fast:
        #if there is no cycle, fast reaches the end of list
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

#RT: O(n) --> if there is no cycle we reach the end of the list by traversing n/2 nodes with fast pointer
#SC: O(1) --> we only store slow and fast pointers, so constant amount of storage regardless of
#             how long the list is
