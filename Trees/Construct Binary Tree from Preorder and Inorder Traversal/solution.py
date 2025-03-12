# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { value: i for i, value in enumerate(inorder) }
        nodes = { value: TreeNode(value) for value in preorder }
        n = len(inorder)

        preorder_idx = 0
        def dfs(l, r):
            nonlocal preorder_idx  
            if l > r:
                return None
            
            value = preorder[preorder_idx]
            node = nodes[value]
            inorder_idx = inorder_indices[value]

            preorder_idx += 1
            node.left = dfs(l, inorder_idx  - 1)
            node.right = dfs(inorder_idx + 1, r)

            return node
        
        return dfs(0, n-1)
            

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { value: i for i, value in enumerate(inorder) }
        n = len(inorder)

        preorder_idx = 0
        def dfs(l, r):  # * Preorder traversal
            nonlocal preorder_idx
            if l > r:
                return None
            
            value = preorder[preorder_idx]
            node = TreeNode(value)
            inorder_idx = inorder_indices[value]

            preorder_idx += 1
            node.left = dfs(l, inorder_idx  - 1)
            node.right = dfs(inorder_idx + 1, r)

            return node
        
        return dfs(0, n-1)
            

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { value: i for i, value in enumerate(inorder) }
        n = len(inorder)
        preorder_idx = [0]

        def dfs(l, r, preorder_idx):  # * Preorder traversal
            if l > r:
                return None
            
            value = preorder[preorder_idx[0]]
            node = TreeNode(value)
            inorder_idx = inorder_indices[value]

            preorder_idx[0] += 1
            node.left = dfs(l, inorder_idx  - 1, preorder_idx)
            node.right = dfs(inorder_idx + 1, r, preorder_idx)

            return node
        
        return dfs(0, n-1, preorder_idx)
            

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { value: i for i, value in enumerate(inorder) }
        n = len(inorder)
        
        def dfs(pre_left, pre_right, in_left, in_right): # * preorder traversal + divide and conquer
            if in_left > in_right or pre_left > pre_right:
                return None
            
            value = preorder[pre_left]
            node = TreeNode(value)
            inorder_idx = inorder_indices[value]

            n_nodes_on_left = inorder_idx - in_left
            
            node.left = dfs(
                pre_left + 1, 
                pre_left + n_nodes_on_left,
                in_left,
                inorder_idx - 1
            )
            node.right = dfs(
                pre_left + n_nodes_on_left + 1, 
                pre_right,
                inorder_idx + 1,
                in_right
            )

            return node
        
        return dfs(0, n-1, 0, n-1)
            

            