# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        self.inorder_traverse(root, values)
        
        return values[k - 1]
    
    def inorder_traverse(self, root, results):
        if not root:
            return
        
        self.inorder_traverse(root.left, results)
        results.append(root.val)
        self.inorder_traverse(root.right, results)
        