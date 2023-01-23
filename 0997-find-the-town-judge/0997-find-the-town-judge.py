class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1 ## edge case
        s, d = set(list(range(1, n+1))), defaultdict(lambda:0) ## trust nobody, trusted by number of people
        for p1, p2 in trust:
            if p1 in s: 
                s.remove(p1)
            d[p2] += 1
        for p in s:
            if p in d and d[p]==n-1:
                return p
        return -1