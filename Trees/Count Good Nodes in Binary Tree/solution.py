# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_val):
            if not root:
                return 0
            
            good_nodes = 0
            if root.val >= max_val:
                good_nodes = 1
            
            max_val = max(root.val, max_val)
            good_nodes += dfs(root.left, max_val)
            good_nodes += dfs(root.right, max_val)

            return good_nodes
        
        return dfs(root, float("-inf"))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        good_nodes = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                good_nodes += 1
            
            max_val = max(node.val, max_val)
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
            
        return good_nodes