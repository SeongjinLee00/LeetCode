"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results=[[] for _ in range(1000)]
        
        q=deque([[root,0]])
        while q:
            now, depth=q.popleft()
            if not now:
                continue
            results[depth].append(now.val)
            for next in now.children:
                q.append([next,depth+1])
        
        for i in range(999,-1,-1):
            if results[i]:
                return results[:i+1]