class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        start = {}
        end = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                start[nums[i]] = i
                end[nums[i]]= i

            else:
                count[nums[i]] +=1
                end[nums[i]] = i

        result = []

        maximum = max(count.values())

        for i , j in count.items():
            if j == maximum:
                total = end[i] - start[i] + 1
                result.append(total)

        return min(result)