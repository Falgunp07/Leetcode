class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        limit = len(candyType) // 2
        unique_types = len(set(candyType))
        
        return min(limit, unique_types)