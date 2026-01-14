# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def helper(root, skip):
            if not root:
                return 0
            
            if not skip:
                return root.val + helper(root.left, True) + helper(root.right, True)

            return max(
                helper(root.left, False) + helper(root.right, False),
                helper(root.left, False) + helper(root.right, True),
                helper(root.left, True) + helper(root.right, False),
                helper(root.left, True) + helper(root.right, True)
            )

        return max(helper(root, False), helper(root, True))



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def postorder(root):
            if not root:
                return [0, 0]
            
            left_pair = postorder(root.left)
            right_pair = postorder(root.right)

            with_root = root.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)

            return [with_root, without_root]
        
        return max(postorder(root))


