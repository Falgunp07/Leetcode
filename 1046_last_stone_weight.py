class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        stones1 = heapify(stones)
        while len(stones) > 1:

            first = heappop(stones)*-1
            second = heappop(stones)*-1
            left = abs(first-second)
            heappush(stones,left*-1)

        return -stones[0]