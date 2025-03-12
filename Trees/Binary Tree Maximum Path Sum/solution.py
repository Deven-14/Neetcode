# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root.left and not root.right:
                return root.val, root.val
            
            elif not root.left:
                right_sum, right_max = dfs(root.right)
                path_sum = root.val + right_sum
                return max(path_sum, root.val), max(root.val, right_max, path_sum)
            
            elif not root.right:
                left_sum, left_max = dfs(root.left)
                path_sum = root.val + left_sum
                return max(path_sum, root.val), max(root.val, left_max, path_sum)
            
            left_sum, left_max = dfs(root.left)
            right_sum, right_max = dfs(root.right)
            path_sum = root.val + left_sum + right_sum

            return (
                max(
                    root.val,
                    left_sum + root.val,
                    right_sum + root.val
                ), max(
                    root.val,
                    left_max,
                    right_max,
                    left_sum + root.val,
                    right_sum + root.val,
                    path_sum
                )
            )
        
        tree_sum, max_path_sum = dfs(root)
        return max_path_sum

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, float("-inf")
            
            left_sum, left_max = dfs(root.left)
            right_sum, right_max = dfs(root.right)
            path_sum = root.val + left_sum + right_sum

            return (
                max(
                    root.val,
                    left_sum + root.val,
                    right_sum + root.val
                ), max(
                    root.val,
                    left_max,
                    right_max,
                    left_sum + root.val,
                    right_sum + root.val,
                    path_sum
                )
            )
        
        tree_sum, max_path_sum = dfs(root)
        return max_path_sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, float("-inf")
            
            left_sum, left_max = dfs(root.left)
            right_sum, right_max = dfs(root.right)

            return (
                max(
                    root.val,
                    left_sum + root.val,
                    right_sum + root.val
                ), max(
                    root.val,
                    left_max,
                    right_max,
                    left_sum + root.val,
                    right_sum + root.val,
                    root.val + left_sum + right_sum
                )
            )
        
        tree_sum, max_path_sum = dfs(root)
        return max_path_sum

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, float("-inf")
            
            left_sum, left_max = dfs(root.left)
            right_sum, right_max = dfs(root.right)

            # path_sum, can either be only root or root + left or root + right
            path_sum = max(root.val, left_sum + root.val, right_sum + root.val)

            # max_path_sum, can be the max of all these conditions
            max_path_sum = max(
                    root.val,
                    left_max,
                    right_max,
                    left_sum + root.val,
                    right_sum + root.val,
                    root.val + left_sum + right_sum
                )

            return path_sum, max_path_sum
        
        tree_sum, max_path_sum = dfs(root)
        return max_path_sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, float("-inf")
            
            left_sum, left_max = dfs(root.left)
            right_sum, right_max = dfs(root.right)

            # path_sum, can either be only root or root + left or root + right
            path_sum = max(root.val, left_sum + root.val, right_sum + root.val)

            # max_path_sum, can be the max of all these conditions
            max_path_sum = max(
                    path_sum,
                    left_max,
                    right_max,
                    root.val + left_sum + right_sum
                )

            return path_sum, max_path_sum
        
        tree_sum, max_path_sum = dfs(root)
        return max_path_sum

        

