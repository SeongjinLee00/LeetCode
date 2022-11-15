class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        numbers=[i*i for i in range(int(sqrt(c))+1)]
        
        i=0
        j=len(numbers)-1
        
        while True:
            if numbers[i]+numbers[j]==c:
                return True
            elif numbers[i]+numbers[j]>c:
                j-=1
            elif numbers[i]+numbers[j]<c:
                i+=1
            
            if i>j:
                return False