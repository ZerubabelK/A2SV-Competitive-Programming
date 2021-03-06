# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            #nonlocal _pbool, _qbool
            if not node or node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            leftOrRight = left or right
            return leftOrRight
        return dfs(root)