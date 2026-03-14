class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        result = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c +=1
            else:
                c = 1
            result = max(result,c)

        return result