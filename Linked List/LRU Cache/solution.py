from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # idea is to use singly linked list with move to end functionality with dictionary
        # we have this inbuild in ordered dict
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        



class Node:

    def __init__(self, key: int, value: int, prev = None, next = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev # needed coz of move to end functionality

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
    
    def move_to_end(self, node):
        if self.tail == node:
            return 
        elif self.head == self.tail == node: # single node
            return
        
        if self.head == node:
            next_node = node.next
            next_node.prev = None
            self.head = next_node
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        
    def popleft(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = self.tail = None
            return node
        
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        
        return node
    
    def print_list(self):
        node = self.head
        l = []
        while node:
            l.append((node.key, node.value))
            node = node.next
        print(l)

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        print(key)
        self.dll.move_to_end(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.dll.move_to_end(self.cache[key])
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.dll.append(node)

        if len(self.cache) > self.capacity:
            node = self.dll.popleft()
            del self.cache[node.key]
