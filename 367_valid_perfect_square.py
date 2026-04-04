class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 2
        r = num // 2
        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False