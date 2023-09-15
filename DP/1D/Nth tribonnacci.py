# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    #recursion
    def solve1(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        return self.solve1(n-1)+self.solve1(n-2)+self.solve1(n-3)
    
    #memoization
    def solve2(self,n,dp):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        if dp[n]!=-1:
            return dp[n]
        temp=self.solve2(n-1,dp)+self.solve2(n-2,dp)+self.solve2(n-3,dp)
        dp[n]=temp
        return temp
    
    #tabulation
    def solve3(self,n,dp):
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]

    #space optimization
    def solve(self,n):
        if n==0:
            return 0
        prev1=0
        prev2=1
        prev3=1

        for j in range(3,n+1):
            curr=prev1+prev2+prev3
            prev1=prev2
            prev2=prev3
            prev3=curr
        return prev3
    
    
    def tribonacci(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return self.solve(n)
        
