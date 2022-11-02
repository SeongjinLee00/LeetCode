class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sumOfDigit(n):
            ret=0
            
            while n>0:
                ret+=n%10
                n//=10
            
            return ret
        
        arr=[]
        
        m=n
        
        while n>0:
            arr.append(n%10)
            n//=10
        
        tmp=0
        i=0
        while True:
            if sumOfDigit(m+tmp)<=target:
                return tmp
            
            if i==0:
                tmp+=(10-arr[i])*(10**i)
            else:
                tmp+=(10-arr[i]-1)*(10**i)
            
            i+=1