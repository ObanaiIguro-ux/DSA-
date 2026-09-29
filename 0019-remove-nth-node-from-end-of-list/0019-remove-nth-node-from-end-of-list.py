# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy    #left ptr
        right = head    #right ptr
        #move right n steps
        for _ in range(n):
            right = right.next
        #move pointers together
        while right:    
            left = left.next
            right = right.next
        #remove nth node
        left.next = left.next.next
        return dummy.next