# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
           
            first = current.next
            second = current.next.next
						# swap
            current.next = second
            first.next = second.next
            second.next = first

            # current node to the previous second node place.
            current = current.next.next
        return dummy.next