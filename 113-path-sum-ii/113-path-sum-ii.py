# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        def dfs(node,s,path):
            print(path)

            if (not node.left) and (not node.right) and s==targetSum:
                ans.append(path)
                return
            
            if node.left: dfs(node.left, s+node.left.val, path+[node.left.val])
            if node.right: dfs(node.right, s+node.right.val, path+[node.right.val])
        
        dfs(root, root.val, [root.val])
        
        return ans