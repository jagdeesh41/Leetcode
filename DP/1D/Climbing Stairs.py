# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    #recursion
    def solve1(self,n):
        if n==0:
            return 1
        if n==1:
            return 1
        return self.solve1(n-1)+self.solve1(n-2)
    
    #memoization
    def solve2(self,n,dp):
        if n==0:
            return 1
        if n==1:
            return 1
        if dp[n]!=-1:
            return dp[n]
        l=self.solve2(n-1,dp)
        r=self.solve2(n-2,dp)
        dp[n]=l+r
        return dp[n]
    
    #tabulation
    def solve3(self,n,dp):
        dp[0]=1
        dp[1]=1
        for j in range(2,n+1):
            dp[j]=dp[j-1]+dp[j-2]
        return dp[n]


    #space optimization

    def solve(self,n):
        prev1=1
        prev2=1
        for j in range(2,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr
        return prev2
        


    
    def climbStairs(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return self.solve(n)

        
