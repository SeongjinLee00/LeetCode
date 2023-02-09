class Solution:
    def distinctNames(self, xs: List[str]) -> int:
        idx = defaultdict(lambda: len(idx))
        grp = defaultdict(set)
        for x in xs:
            grp[x[0]].add(idx[x[1:]])
        n = 0
        for a, b in combinations(grp.values(), 2):
            d = len(a&b)
            n += (len(a)-d) * (len(b)-d)
        return n * 2