# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer=0
        
        def dfs(now, currmax):
            nonlocal answer
            if now:
                if now.val>=currmax:
                    answer+=1
                    currmax=now.val
                    dfs(now.left, currmax)
                    dfs(now.right, currmax)
                else:
                    dfs(now.left, currmax)
                    dfs(now.right, currmax)
        
        dfs(root,root.val)
        return answer