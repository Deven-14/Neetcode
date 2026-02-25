from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = head
        node2 = head.next
        while node2:
            divisor = gcd(node1.val, node2.val)
            gcd_node = ListNode(divisor, node2)
            node1.next = gcd_node
            node1, node2 = node2, node2.next
        
        return head