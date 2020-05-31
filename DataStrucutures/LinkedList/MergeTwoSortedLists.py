#Merge Two Sorted Lists
#LC 21

"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


def mergeTwoLists(l1,l2):
    mergedList = ListNode(0)
    def merge(l1,l2,head):
        if not l1:
            head.next = l2
            return
        if not l2:
            head.next = l1
            return
        if l1.val < l2.val:
            head.next = ListNode(l1.val)
            merge(l1.next,l2,head.next)
        elif l2.val < l1.val:
            head.next = ListNode(l2.val)
            merge(l1,l2.next,head.next)
        elif l1.val == l2.val:
            head.next = ListNode(l1.val)
            head.next.next = ListNode(l2.val)
            merge(l1.next,l2.next,head.next.next)
    merge(l1,l2,mergedList)
    mergedList = mergedList.next
    return mergedList

#RT: O(n+m) where n and m are lengths of l1 and l2 --> we recuse on all nodes in both Lists
#SC: O(n+m) --> we maintain a new list and do not modify l1 and l2. 
