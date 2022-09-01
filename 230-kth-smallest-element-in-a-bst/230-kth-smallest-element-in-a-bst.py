# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        cnt=0
        ans=123123
        def inorder(node):
            nonlocal cnt
            nonlocal ans

            if node.left: inorder(node.left)
            cnt+=1
            if cnt==k:
                ans = node.val
            if node.right: inorder(node.right)
        
        inorder(root)
        return ans