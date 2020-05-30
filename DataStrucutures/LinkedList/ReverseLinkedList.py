#Reverse a singly linked list
#LC 206

"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

def reverseListRecursive(head):
    #A single node is already reversed, and a null node is also already reversed
    if head.next == None or head == None:
        return head
    #assume function works and reverse the rest of the list
    reveresedRest = reverseListRecursive(head.next)
    #set next node to point to current node
    head.next.next = head
    #set current node to point to None
    head.next = None
    return reveresedRest
