class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(r,c):
            if(r,c)==(m-1,n-1):
                return 1

            elif r ==m or c==n :
                return 0
        
            return dp(r+1,c) + dp(r,c+1)
        return dp(0,0)

