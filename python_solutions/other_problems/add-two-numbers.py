# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_t, sum_t = 0, 0
        dummynode = ListNode(0)
        tailnode = dummynode
        result = None
        while l1 or l2:
            first = 0
            second = 0
            if l1:
                first = l1.val
            if l2:
                second = l2.val
            sum_t = (first+second+carry_t)
            carry_t = (sum_t)//10
            sum_t = sum_t%10
            temp = ListNode(sum_t)
            tailnode.next = temp
            tailnode = tailnode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry_t:
            temp = ListNode(carry_t)
            tailnode.next = temp
        result = dummynode.next
        dummynode.next = None
        return result
        
