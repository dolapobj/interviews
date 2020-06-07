#Reversed Linked List II
#LC 92
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

#Find m, reverse until n
def reverseBetween(head,m,n):
    dummy = ListNode(next = head)
    def reverse(head,end):
        if head == end:
            return head
        reversedRest = reverse(head.next,end)
        head.next.next = head
        head.next = None
        return reversedRest
    if not head or not head.next:
        return head
    #find mth node
    mcount,ncount = 0,0
    mpoint,npoint = dummy,dummy
    mtemp,ntemp = None,None
    while mcount != m:
        if mcount == m-1:
            mtemp = mpoint.next
        mpoint = mpoint.next
        mcount +=1
    #find nth node
    while ncount != m:
        npoint = npoint.next
        ncount +=1
    ntemp = npoint.next
    #ntemp == node n+1, mtemp == node m-1
    mtemp.next = reverse(mpoint,npoint)
    mpoint.next = ntemp
    return dummy.next

#RT: O(n) --> traverse all nodes
#SC: O(n) --> because of recursive implementation of reverse. Could also do iteratively to reduce memory.
