# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        cnt=0
        # if curr_node == None or curr_node.next == None:
        #     return curr_node
        while curr_node!=None:
            curr_node=curr_node.next
            cnt+=1
        middle = int(cnt/2)+1
        curr_node = head
        cnt=0
        while curr_node!=None:
            curr_node=curr_node.next
            cnt+=1
            if cnt==middle-1:
                break
        return curr_node