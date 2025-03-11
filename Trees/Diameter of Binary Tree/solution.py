# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return 0, 0
            
            left_depth, left_diameter = helper(root.left)
            right_depth, right_diameter = helper(root.right)
            root_depth = 1+max(left_depth, right_depth)
            root_diameter = max(left_diameter, right_diameter, left_depth + right_depth)

            return root_depth, root_diameter
        
        root_depth, root_diameter = helper(root)
        return root_diameter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(root):
            if not root:
                return 0
            
            nonlocal diameter # not advisable, but to know the concept
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            diameter = max(diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        root_depth = dfs(root)
        return diameter


# for iteratively
# first get the depth of the tree for each node, store it in a dictionary
# then go another iteration to get the diameter of the tree for each node