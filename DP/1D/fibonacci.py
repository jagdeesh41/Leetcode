# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    #recursion
    def solve(self,n):
      if n==0:
        return 0
      if n==1:
        return 1
      return self.solve(n-1)+self.solve(n-2)

    #memoization
    def solve1(self,n,dp):
      if n==0:
        return 0
      if n==1:
        return 1
      if dp[n]!=-1:
        return dp[n]
      temp=self.solve1(n-1,dp)+self.solve1(n-2,dp)
      dp[n]=temp
      return temp
    
    #tabulation
    def solve2(self,n,dp):
      if n<=1:
        return n
      dp[0]=0
      dp[1]=1
      for j in range(2,n+1,1):
        dp[j]=dp[j-1]+dp[j-2]
      return dp[n]


    #space optimization
    def solve3(self,n):
      if n<=1:
        return n
      prev1=0
      prev2=1
      curr=-1
      for j in range(2,n+1):
        curr=prev1+prev2
        prev1=prev2
        prev2=curr
      return prev2

      
    

    def fib(self, n: int) -> int:
      dp=[-1 for i in range(n+1)]
      return self.solve3(n)


        
