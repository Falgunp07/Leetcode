class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_set = set(range(1, n + 1))
        actual_set = set(nums)

        result = list(expected_set - actual_set)
        return result