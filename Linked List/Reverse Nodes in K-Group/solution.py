# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, start, stop):
        node = start
        node.prev = None
        prev = None
        while node != stop:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        start.next = stop
        return prev
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head

        n = k
        while n and fast:
            fast = fast.next
            n -= 1
        
        reversed_list_head = self.reverse(slow, fast)
        reversed_list_tail = slow

        while fast:
            
            slow = slow.next # slow is now connected to start of next sub list

            n = k
            while n and fast:
                fast = fast.next
                n -= 1
            
            if n > 0:
                break
            
            reversed_sub_list_head = self.reverse(slow, fast)
            reversed_list_tail.next = reversed_sub_list_head
            reversed_list_tail = slow
        
        return reversed_list_head

