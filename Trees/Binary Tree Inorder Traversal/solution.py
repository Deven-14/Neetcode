# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def helper(node):
            if not node:
                return
            
            helper(node.left)
            nodes.append(node.val)
            helper(node.right)
        
        helper(root)
        return nodes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        nodes = []
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            nodes.append(node.val)
            node = node.right
        
        return nodes
