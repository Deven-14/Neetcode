# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(root):
            if not root:
                return 0
            
            nonlocal is_balanced
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) > 1:
                is_balanced = False
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return is_balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0, True
            
            left_height, left_is_balanced = dfs(root.left)
            right_height, right_is_balanced = dfs(root.right)
            is_balanced = abs(left_height - right_height) <= 1
            
            height = 1 + max(left_height, right_height)
            return height, is_balanced and left_is_balanced and right_is_balanced
        
        height, is_balanced = dfs(root)
        return is_balanced

