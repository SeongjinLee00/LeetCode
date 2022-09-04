# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results=defaultdict(lambda:defaultdict(list))
        
        q=deque([[root,0,0]])
        
        while q:
            now, row, col = q.popleft()
            results[col][row].append(now.val)
            
            if now.left:
                q.append([now.left,row+1,col-1])
            if now.right:
                q.append([now.right,row+1,col+1])
        
        m=min(results)
        M=max(results)
        
        ret=[[] for _ in range(M-m+1)]
        
        for k1,v1 in results.items():
            for k2,v2 in results[k1].items():
                ret[k1-m].extend(sorted(v2))
                
        return ret