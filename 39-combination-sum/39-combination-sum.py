class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]
        
        def backtrack(s,path):
            if s>=target:
                if s==target:
                    output.append(path)
                return
            
            for number in candidates:
                if path and number<path[-1]:
                    continue
                backtrack(s+number,path+[number])
                
        backtrack(0,[])
        
        return output