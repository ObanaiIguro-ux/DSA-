# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        #initializes slow and fast, both pointing to the head of the list
        slow, fast = head, head

        #traverse as long as fast and its nxt node are not NULL
        while fast!=None and fast.next!=None:
            slow = slow.next #slow move 1 step
            fast = fast.next.next #fast moves 2 steps

        #loop ends, slow pointer will be at middle of the list
        return slow
