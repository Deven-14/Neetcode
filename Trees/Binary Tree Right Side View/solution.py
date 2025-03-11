# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        right_side_view = []
        while queue:
            curr_level_queue = queue
            queue = deque()
            right_side_view.append(curr_level_queue[-1].val)

            while curr_level_queue:
                node = curr_level_queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return right_side_view
