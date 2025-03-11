# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root, k):
            if not root:
                return 0, None

            nleft_nodes, kth_node = dfs(root.left, k)
            if kth_node:
                return nleft_nodes + 1, kth_node

            if nleft_nodes + 1 == k:
                return nleft_nodes + 1, root
            
            nright_nodes, kth_node = dfs(root.right, k - (1 + nleft_nodes))
            
            return 1 + nleft_nodes + nright_nodes, kth_node
        
        root_nth_node, kth_node = dfs(root, k)
        return kth_node.val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative inorder traversal
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            
            k -= 1
            if k == 0:
                return node.val
            
            node = node.right
