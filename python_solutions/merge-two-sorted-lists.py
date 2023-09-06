# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Learning1: to avoid the first head check(if else, 
        directly do the check in while loop) using a dummy head at end return head.next
        """

        head_merged = ListNode()
        tail = head_merged
        cnt = 0
        while(list1!= None and list2!= None):
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        if list1!=None:
            tail.next = list1
        if list2!=None:
            tail.next = list2
        return head_merged.next