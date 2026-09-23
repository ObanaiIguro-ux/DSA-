class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Traverse the list with two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the two pointers will meet
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle
        return False