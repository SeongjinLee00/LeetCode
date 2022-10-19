class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(sorted(words))
        return sorted(d, key = lambda x: d.get(x), reverse = True)[:k]