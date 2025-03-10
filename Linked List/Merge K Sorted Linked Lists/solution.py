# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = mnode = ListNode()

        queue = []
        i = 0
        for node in lists:
            heapq.heappush(queue, (node.val, i, node))
            i += 1
        
        while queue:
            value, _, node = heapq.heappop(queue)
            if node.next:
                heapq.heappush(queue, (node.next.val, i, node.next))
                i += 1

            mnode.next = node
            mnode = mnode.next
        
        return merged_list.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrap:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = mnode = ListNode()

        min_heap = []
        for node in lists:
            heapq.heappush(min_heap, NodeWrap(node))
        
        while min_heap:
            node_wrap = heapq.heappop(min_heap)
            if node_wrap.node.next:
                heapq.heappush(min_heap, NodeWrap(node_wrap.node.next))

            mnode.next = node_wrap.node
            mnode = mnode.next
        
        return merged_list.next
            
        
