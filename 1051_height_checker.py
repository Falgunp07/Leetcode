class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height1 = sorted(heights)
        sum1 = 0

        for i in range(len(heights)):
            if height1[i] != heights[i]:
                sum1+=1
        return sum1