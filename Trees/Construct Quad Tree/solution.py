"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def are_equal(i, j, length):
            ele = grid[i][j]

            for k in range(i, i + length):
                for l in range(j, j + length):
                    if grid[k][l] != ele:
                        return False, False
            
            return bool(ele), True
        
        def helper(i, j, length):
            if length == 0:
                return None

            val, is_leaf = are_equal(i, j, length)
            if is_leaf:
                return Node(val, is_leaf, None, None, None, None)
            
            mid = length // 2
            top_left = helper(i, j, mid)
            top_right = helper(i, j+mid, mid)
            bottom_left = helper(i+mid, j, mid)
            bottom_right = helper(i+mid, j+mid, mid)

            node = Node(val, is_leaf, top_left, top_right, bottom_left, bottom_right)
            return node
        
        return helper(0, 0, n)


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        def helper(i, j, length):
            if length == 1:
                return Node(grid[i][j] == 1, True)
            
            mid = length // 2
            top_left = helper(i, j, mid)
            top_right = helper(i, j+mid, mid)
            bottom_left = helper(i+mid, j, mid)
            bottom_right = helper(i+mid, j+mid, mid)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True)

            return Node(False, False, top_left, top_right, bottom_left, bottom_right)
        
        return helper(0, 0, n)
