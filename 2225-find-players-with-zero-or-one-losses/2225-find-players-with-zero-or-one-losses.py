class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose=defaultdict(int)
        ret=[[],[]]
        players=set()
        for w,l in matches:
            lose[l]+=1
            players.add(w)
            players.add(l)
            
        for player in players:
            if lose[player]==0:
                ret[0].append(player)
            elif lose[player]==1:
                ret[1].append(player)
        
        ret[0].sort()
        ret[1].sort()
        return ret