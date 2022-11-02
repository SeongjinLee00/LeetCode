class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def match(word1, word2):
            count = 0
            for w1, w2 in zip(word1, word2):
                if w1 != w2:
                    count += 1
                if count > 2:
                    return False
            return True
        
        res = []
        for query in queries:
            for ele in dictionary:
                if match(query, ele):
                    res.append(query)
                    break
        
        return res