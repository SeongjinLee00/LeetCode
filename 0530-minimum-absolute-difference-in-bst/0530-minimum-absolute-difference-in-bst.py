# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        q=[root]
        numbers=[]
        
        while q:
            now=q.pop()
            numbers.append(now.val)
            if now.left:
                q.append(now.left)
            if now.right:
                q.append(now.right)
        
        ans=999999999
        numbers.sort()
        for i in range(len(numbers)-1):
            ans=min(ans,numbers[i+1]-numbers[i])
        
        return ans