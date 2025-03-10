# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = node3 = ListNode()

        node1 = l1
        node2 = l2
        carry_over = 0

        while node1 and node2:
            carry_over, value = divmod(node1.val + node2.val + carry_over, 10)
            node3.next = ListNode(value)
            node3 = node3.next
            node1 = node1.next
            node2 = node2.next
        
        node4 = node1 or node2

        while node4:
            carry_over, value = divmod(node4.val + carry_over, 10)
            node3.next = ListNode(value)
            node3 = node3.next
            node4 = node4.next
        
        if carry_over:
            node3.next = ListNode(carry_over)
        
        return l3.next