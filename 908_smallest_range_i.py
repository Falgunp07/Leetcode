class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        high = max(nums)
        low = min(nums)
        diff = high - low
        result = diff - 2 * k

        return max(0, result)
        