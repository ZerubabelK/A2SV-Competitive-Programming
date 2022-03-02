# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(root,arr):
            if root == None:
                return
            
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right,arr)
            
        inorder(root, arr)
        
        return arr[k - 1]