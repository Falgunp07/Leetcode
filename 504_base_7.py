class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        res_list = []
        
        while num > 0:
            remainder = num % 7
            res_list.append(str(remainder))
            num //= 7
            
        result = "".join(res_list[::-1])
        return "-" + result if is_negative else result