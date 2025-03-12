# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return f"$#"
            
            return f"${root.val}{preorder(root.left)}{preorder(root.right)}"
        
        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def preorder(nums):
            value = nums.popleft()
            if value == "#":
                return None
            
            node = TreeNode(int(value))
            node.left = preorder(nums)
            node.right = preorder(nums)

            return node
        
        nums = deque(data.split("$"))
        nums.popleft()
        return preorder(nums)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(root, nums):
            if not root:
                nums.append("#")
                return 
            
            nums.append(str(root.val))
            preorder(root.left, nums)
            preorder(root.right, nums)
        
        nums = []
        preorder(root, nums)
        return "$".join(nums)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def preorder(nums):
            value = nums.popleft()
            if value == "#":
                return None
            
            node = TreeNode(int(value))
            node.left = preorder(nums)
            node.right = preorder(nums)

            return node
        
        nums = deque(data.split("$"))
        return preorder(nums)
            
# * If you are doing it using bfs then use a single while loop and append the values to the string