class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        
        for item in strs:
            sorted_str=sorted(list(item))
            d[tuple(sorted_str)].append(item)
        
        return d.values()
                