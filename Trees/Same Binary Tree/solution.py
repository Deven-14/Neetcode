# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                
        stack = [(p, q)]
        while stack:
            pnode, qnode = stack.pop()
            if not pnode and not qnode:
                continue
            elif not pnode or not qnode:
                return False

            if pnode.val != qnode.val:
                return False
                
            stack.append((pnode.left, qnode.left))
            stack.append((pnode.right, qnode.right))
        
        return True
        