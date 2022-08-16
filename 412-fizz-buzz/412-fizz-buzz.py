class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[""]*n
        for i in range(1,n+1):
            if not i%3:
                ans[i-1]+="Fizz"
                if not i%5:
                    ans[i-1]+="Buzz"
                continue
            if not i%5:
                ans[i-1]+="Buzz"
                continue
            ans[i-1]+=str(i)
        
        return ans