# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ret=''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ret+=str(root.val)
        
        
        if root.left:
            self.ret+='('
            self.tree2str(root.left)
            self.ret+=')'
        if not root.left and root.right:
            self.ret+='()'
        if root.right:
            self.ret+='('
            self.tree2str(root.right)
            self.ret+=')'
        
        return self.ret