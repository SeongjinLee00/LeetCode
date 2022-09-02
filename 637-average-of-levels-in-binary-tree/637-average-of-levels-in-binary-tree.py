# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q=deque([[root,0]])
        results=defaultdict(lambda:[0,0])
        
        maxlevel=0
        while q:
            now, level=q.popleft()
            results[level][0]+=1
            results[level][1]+=now.val
            maxlevel=max(level,maxlevel)
            if now.left:
                q.append([now.left, level+1])
            if now.right:
                q.append([now.right, level+1])
                
        ret=[]
        
        for i in range(maxlevel+1):
            ret.append(results[i][1]/results[i][0])
            
        return ret