#Reverse a singly linked list
#LC 206

"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

def reverseListRecursive(head):
    #A single node is already reversed, and a null node is also already reversed
    if head == None or head.next == None:
        return head
    #assume function works and reverse the rest of the list
    reveresedRest = reverseListRecursive(head.next)
    #set next node to point to current node
    head.next.next = head
    #set current node to point to None
    head.next = None
    return reveresedRest

#RT: O(n) --> we visit all nodes in the list
#SC: O(n) --> we store space in the stack for each node because of the
#             recursive calls

def reverseListIterative(head):
    prev = None
    curr = head
    while curr:
        #store next node before moving pointers
        temp = curr.next
        #set next node points to previous! this is reversing!
        curr.next = prev
        #now lets reset our prev and curr nodes for next iteration!
        prev = curr
        curr = temp
    return prev

#RT: O(n) --> we traverse all nodes in the graph
#SC: O(1) --> we only store our two pointers to prev and curr.
