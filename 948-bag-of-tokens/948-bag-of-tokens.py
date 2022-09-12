# class Solution:
#     def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
#         tokens.sort()
#         tokens=deque(tokens)
        
#         score=0
#         while True:
#             while power>=tokens[0]:
#                 power-=tokens.popleft()
#                 score+=1
#                 if not tokens:
#                     return score
#             if score and len(tokens)>=2:
#                 power+=tokens.pop()
#                 score-=1
        
#         return score

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans