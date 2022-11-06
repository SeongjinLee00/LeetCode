class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1: # k=1일때는 necklace 가능
            return min(s[i:] + s[:i] for i in range(len(s)))
        else: # k>=2 일때는 두 수를 swap하는 것이 가능해지고, 따라서 s의 모든 permutation 가능
            return ''.join(sorted(s))