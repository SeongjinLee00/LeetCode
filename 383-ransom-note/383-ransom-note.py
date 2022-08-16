class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(97,97+26):
            if ransomNote.count(chr(i))>magazine.count(chr(i)):
                return False
        return True
        