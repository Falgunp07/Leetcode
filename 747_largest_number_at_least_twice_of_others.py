class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max2 = -1
        index1 = -1
        
        for i, n in enumerate(nums):
            if n > max1:
                max2 = max1
                max1 = n
                index1 = i
            elif n > max2:
                max2 = n
        if max1 >= 2 * max2:
            return index1
        
        return -1