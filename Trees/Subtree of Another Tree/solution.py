# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfsIsSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            if not dfsIsSameTree(p.left, q.left):
                return False
            
            if not dfsIsSameTree(p.right, q.right):
                return False
            
            return True
        
        def dfsIsSubTree(root, sub_root):
            if not root:
                return False
            
            if root.val == sub_root.val and dfsIsSameTree(root, sub_root):
                return True
            
            return (
                dfsIsSubTree(root.left, sub_root)
                or dfsIsSubTree(root.right, sub_root)
            )
        
        if not root and not sub_root:
            return True
        elif not root and sub_root:
            return False
        
        return dfsIsSubTree(root, subRoot)

# * O(n * m) solution

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(root):
            if not root:
                return "$#"
            
            return "$" + str(root.val) + serialize(root.left) + serialize(root.right)
        
        root_serialized = serialize(root)
        sub_root_serialized = serialize(subRoot)

        return sub_root_serialized in root_serialized

# * O(n + m) solution

# instead of using "in" operator, we can use KMP algorithm to find the substring in the string or the Z algorithm
# to find the substring in the string. Both of these algorithms have O(n + m) time complexity.