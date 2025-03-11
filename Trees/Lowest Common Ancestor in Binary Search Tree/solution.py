# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p
        
        def dfs(root):
            if not root:
                return None
            
            if root.val > q.val: # implies root.val > p.val
                return dfs(root.left)
            elif root.val < p.val:
                return dfs(root.right)
            
            # p.val <= root.val <= q.val
            return root
        
        return dfs(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p
        
        node = root
        while node:
            if node.val > q.val: # implies root.val > p.val
                node = node.left
            elif node.val < p.val:
                node = node.right
            else: # p.val <= root.val <= q.val
                return node
            