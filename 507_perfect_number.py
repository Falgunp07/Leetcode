class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total_sum = 1
        sqrt = int(num**0.5) + 1
        for i in range(2,sqrt ):
            if num % i == 0:
                total_sum += i 
                if num // i != i:
                    total_sum += num//i

        if total_sum ==num:
            return True

        return False



            
       