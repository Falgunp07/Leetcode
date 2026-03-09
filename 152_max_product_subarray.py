class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right  = 1
        ans = nums[0]

        for i in range(n):
            if left ==0:
                left = 1
            if right ==0:
                right = 1
            
            left *= nums[i]

            right *= nums[n - 1 - i]

            ans = max(ans, max(left, right))


        return ans