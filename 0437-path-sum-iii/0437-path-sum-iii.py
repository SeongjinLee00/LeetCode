# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        ans=0
        d=defaultdict(int)
        d[0]=1
        def dfs(node,partialsum):
            nonlocal ans
            
            partialsum+=node.val
            
            ans+=d[partialsum-sum]
            
            d[partialsum]+=1

            if node.left:
                dfs(node.left,partialsum)
            if node.right:
                dfs(node.right,partialsum)
            
            d[partialsum]-=1
        
        dfs(root,0)
        
        return ans