class Solution:
    def myAtoi(self, s: str) -> int:
        arr=s.split()
        tmp=""
        flag=0
        if not arr:
            return 0
        
        for c in arr[0]:
            if not flag and (c=='+' or c=='-'):
                tmp+=c
            elif c.isnumeric():
                tmp+=c
            else:
                break         
            flag=1
            
        try:
            if int(tmp)>=(2**31): return 2**31-1
            if int(tmp)<-(2**31): return -(2**31)
            return int(tmp)
        except:
            return 0