class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer=[[1]]
        
        for row in range(1,numRows):
            tmp=[0]+answer[row-1]+[0]
            
            tmp2=[]
            for i in range(len(tmp)-1):
                tmp2.append((tmp[i]+tmp[i+1]))
            
            answer.append(tmp2)
        
        return answer