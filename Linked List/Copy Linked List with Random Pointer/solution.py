"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        node = head
        while node:
            nodes[node] = Node(node.val)
            node = node.next
        
        nodes[None] = None
        node = head
        while node:
            nodes[node].next = nodes[node.next]
            nodes[node].random = nodes[node.random]
            node = node.next
        
        return nodes[head]

# 2 pass

# below is 1 pass

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None

        node = head
        while node:
            nodes[node].val = node.val
            nodes[node].next = nodes[node.next]
            nodes[node].random = nodes[node.random]
            node = node.next
        
        return nodes[head]