# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=False
        
        def dfs(now, s):
            nonlocal ans
            
            if s==targetSum and not now.left and not now.right:
                ans=True
                return
            
            if now.left:
                dfs(now.left, s+now.left.val)
            if now.right:
                dfs(now.right, s+now.right.val)
        
        if root:
            dfs(root, root.val)
        
        return ans