#Find Intersection of Two Linked Linked Lists
#LC  160
"""
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
Output: Reference of the node with value = 8
"""

#Find which list longer, and skip forward in the longer list such that
#both lists are the same length.
#then move together at once, and when both nodes are the same we found
#the intersection!

def findIntersection(headA,headB):
    pA,pB = headA, headB
    lenA, lenB = 0,0
    while pA:
        pA = pA.next
        lenA +=1
    while pB:
        pB = pB.next
        lenB +=1
    if lenA > lenB:
        for i in range(lenA - lenB):
            headA = headA.next
    else:
        for i in range(lenB - lenA):
            headB = headB.next

    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

#RT: O(n) --> we traverse all nodes
#SC: O(1) --> we maintain constant memory (2 pointers, and 2 ints)    
