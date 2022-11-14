class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def find(x):
            while x != parent.setdefault(x, x):
                x = find(parent[x])
            return x
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # a stone's row and col is connected by default
        # use ~ to make negative value to distinguish col with row number
        for i, j in stones:
            union(i, ~j)
        
        return len(stones) - len(set(find(x) for x in parent))