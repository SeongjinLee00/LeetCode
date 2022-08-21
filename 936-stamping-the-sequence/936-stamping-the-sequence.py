class Solution:
    def equals(self, target, stamp, i):
        for j, c in enumerate(stamp):
            if not (target[i + j] == c or target[i + j] == '?'):
                return False
        return True
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = [c for c in target]
        N, M = len(target), len(stamp)
        ans = []
        already_in = set()
        for i in range(N - M + 1):
            if self.equals(target, stamp, i):
                for x in range(i, -1, -1):
                    if x in already_in:
                        break
                    already_in.add(x)
                    if self.equals(target, stamp, x):
                        ans.append(x)
                        target[x:x+M] = ['?'] * M
        return ans[::-1] if all([c == '?' for c in target]) else []

print(Solution().movesToStamp('abca','aabcaca'))