# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        # reverse 
        node = list2
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        list2 = prev

        # join
        node1, node2 = head, list2
        while node2:
            node1_next, node2_next = node1.next, node2.next
            node1.next = node2
            node2.next = node1_next
            node1 = node1_next
            node2 = node2_next
        

        
