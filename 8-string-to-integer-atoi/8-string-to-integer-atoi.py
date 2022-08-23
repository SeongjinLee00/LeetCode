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
                flag=1
            elif c.isnumeric():
                tmp+=c
                flag=1
            else:
                break         
        
        try:
            if int(float(tmp))>=(2**31): return 2**31-1
            if int(float(tmp))<-(2**31): return -(2**31)
            return int(float(tmp))
        except:
            return 0