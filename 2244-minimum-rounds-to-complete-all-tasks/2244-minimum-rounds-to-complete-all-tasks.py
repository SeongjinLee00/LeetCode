class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return max(-1,sum(ceil(freq/3) if freq>1 else -inf for freq in Counter(tasks).values()))