#Reorder a Linked List
#LC 143

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

#approach problem in three steps:
#1. find middle of list
#2. reverse the second half of list
#3. reorder list

#basic idea is have two pointers, when fast reaches end, slow will be at middle
def findMiddle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#reverse a linkedList recursively
def reverseList(head):
    if not head or not head.next:
        return head
    reversed = reverseList(head.next)
    head.next.next = head
    head.next = None
    return reversed

#merge two halves together!
def merge(head):
    middle = findMiddle(head)
    head2 = reverseList(middle.next)
    middle.next = None
    while head and head2:
        tmp1 = head.next
        tmp2 = head2.next
        head2.next = head.next
        head.next = head2
        head = tmp1
        head2 = tmp2

#modifies original list in place!
def reorderList:
    if head:
        merge(head)
