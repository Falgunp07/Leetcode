class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for char in s:
            res = res ^ ord(char)
            pass
        for char in t:
            res = res ^ ord(char)
            pass 
        return chr(res)