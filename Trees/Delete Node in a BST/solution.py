# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def search_min_node(self, root):
        node = root
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif not root.left and not root.right:
            root = None
        elif not root.left or not root.right:
            root = root.left or root.right
        else:
            min_node = self.search_min_node(root.right)
            root.right = self.deleteNode(root.right, min_node.val)
            min_node.left, min_node.right = root.left, root.right
            root = min_node
        
        return root