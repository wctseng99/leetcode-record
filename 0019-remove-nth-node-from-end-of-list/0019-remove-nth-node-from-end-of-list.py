# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_length = 0
        curr = head

        while curr:
            # travesal to count the number of node
            node_length += 1 
            curr = curr.next

        curr = head
        count = 0
        target = node_length - n

        if target == 0:
            return head.next
        
        while curr:
            count += 1
            if count == target:
                curr.next = curr.next.next
                break
            curr = curr.next
            
        return head
