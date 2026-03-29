class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        newarr = sorted(set(arr))
        rank = {}

        for index, num in enumerate(newarr):
            rank[num] = index + 1
        return [rank[num] for num in arr]