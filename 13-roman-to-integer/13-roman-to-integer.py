class Solution:
    def romanToInt(self, s: str) -> int:
        ret=0
        ret+=s.count('CM')*900
        s=s.replace('CM','')
        ret+=s.count('M')*1000
        s=s.replace('M','')
        ret+=s.count('CD')*400
        s=s.replace('CD','')
        ret+=s.count('D')*500
        s=s.replace('D','')
        ret+=s.count('XC')*90
        s=s.replace('XC','')
        ret+=s.count('C')*100
        s=s.replace('C','')
        ret+=s.count('XL')*40
        s=s.replace('XL','')
        ret+=s.count('L')*50
        s=s.replace('L','')
        ret+=s.count('IX')*9
        s=s.replace('IX','')
        ret+=s.count('X')*10
        s=s.replace('X','')
        ret+=s.count('IV')*4
        s=s.replace('IV','')
        ret+=s.count('V')*5
        s=s.replace('V','')
        ret+=s.count('I')

        return ret