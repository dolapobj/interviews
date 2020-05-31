#Remove Nth Node from end of Linked List
#lC 19

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

#idea --> store previous n nodes as we recurse down. When we hit
#         the end of the list, we will know the nth, n-2nd, and n-1st nodes
#         From there, we re arrange the pointers.

def removeNth(head,n):
    dummy = ListNode(0,head)
    previousNodes = [dummy]
    if not head:
        return None
    def traverse(head):
        if head.next == None:
            previousNodes[0].next = previousNodes[0].next.next
            return
        if len(previousNodes) == n:
            previousNodes.pop(0)
        previousNodes.append(head)
        traverse(head.next)
    traverse(head)
    return dummy.next

#RT: O(n) --> we traverse all nodes in the list in one pass
#SC: O(n) --> we maintain a list of the previous n nodes
