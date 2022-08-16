class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt=0
        if not num:
            return 0
        while True:
            if num%2:
                num-=1
            else:
                num//=2
            cnt+=1
            if num==0:
                return cnt