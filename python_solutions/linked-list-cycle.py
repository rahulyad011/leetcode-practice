# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head:
            return False
        fast = head.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next!=None:
                    fast = fast.next.next
        return False