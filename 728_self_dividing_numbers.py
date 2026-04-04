

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for num in range(left, right + 1):
            is_valid = True
            
            num_str = str(num)
            
            for char in num_str:
                if char == '0':
                    is_valid = False
                    break
                digit = int(char)
                if num % digit != 0:
                    is_valid = False
                    break
            
            if is_valid:
                result.append(num)
                
        return result