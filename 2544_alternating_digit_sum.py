class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        total_sum = 0
        for i in range(len(s)):
            digit = int(s[i])
            
            if i % 2 == 0:
                total_sum += digit
            else:
                total_sum -= digit
                
        return total_sum