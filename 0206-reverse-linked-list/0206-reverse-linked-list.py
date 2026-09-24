# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        p = None    #previous pointer
        c = head    #current pointer

        while c:       #current
            next_node = c.next
            c.next = p
            p = c
            c = next_node
        return p