# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        left = right = head
        
        # find the mid point 

        while right and right.next:
            left, right = left.next, right.next.next
        
        mid = left

        # reverse the right half

        prev, curr = None, mid

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        reverse_head =  prev

        # update the linked list

        first, second = head, reverse_head

        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop

            next_hop = second.next
            second.next = first
            second = next_hop




        