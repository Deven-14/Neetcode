# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1
        right -= left

        # left node and left previous
        node = head
        left_prev = None
        while left:
            left_prev = node
            node = node.next
            left -= 1
        left_node = node
        if left_prev != None:
            left_prev.next = None
        
        # right node and right next
        node = left_node
        while right:
            node = node.next
            right -= 1
        right_node = node
        right_next = right_node.next
        right_node.next = None

        # reverse
        node = left_node
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        # join
        new_left, new_right = right_node, left_node
        new_right.next = right_next

        if left_prev == None:
            head = new_left
        else:
            left_prev.next = new_left
        
        return head


# * one pass

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= left

        # left node and left previous
        node = head
        left_prev = None
        while left:
            left_prev = node
            node = node.next
            left -= 1
        left_node = node
        if left_prev != None:
            left_prev.next = None
        
        # right node and right next and reverse
        node = left_node
        right_prev = None
        while right:
            next_node = node.next
            node.next = right_prev
            right_prev = node
            node = next_node
            right -= 1

        new_left = right_prev
        right_next = node
        new_right = left_node

        if new_left:

            if left_prev == None:
                head = new_left
            else:
                left_prev.next = new_left

            new_right.next = right_next

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= left

        # left node and left previous
        dummy = ListNode(0, head)
        node = head
        left_prev = dummy
        while left:
            left_prev = node
            node = node.next
            left -= 1

        left_node = node
        left_prev.next = None
        
        # right node and right next and reverse
        node = left_node
        right_prev = None
        while right:
            next_node = node.next
            node.next = right_prev
            right_prev = node
            node = next_node
            right -= 1

        new_left = right_prev
        right_next = node
        new_right = left_node

        left_prev.next = new_left
        new_right.next = right_next

        return dummy.next

