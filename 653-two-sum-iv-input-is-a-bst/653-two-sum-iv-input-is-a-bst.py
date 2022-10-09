class Solution:
    
    def inorder(self, node, arr):
        
            if node.left is not None:
                self.inorder(node.left, arr)
            
            arr.append(node.val)
            
            if node.right is not None:
                self.inorder(node.right, arr)
                
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Go through the entire array in order to find the ordered version of the BST
        
        arr = []
        self.inorder(root, arr)
        
        # perform 2 pointer on this??
        l = 0
        r = len(arr) -1
        
        while l < r:
            s = arr[l] + arr[r]
            if s == k:
                return True
            elif s < k:
                l += 1
            else:
                r-=1
                
        return False