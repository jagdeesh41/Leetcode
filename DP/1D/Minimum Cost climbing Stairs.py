# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    #Recursion
    def solve(self,index,cost):
        if index>=len(cost):
            return 0
        if index==len(cost)-1:
            return cost[-1]
        call1=cost[index]+self.solve(index+1,cost)
        call2=cost[index]+self.solve(index+2,cost)
        mini=min(call1,call2)
        return mini
    
    # memoization
    def solve1(self,index,cost,dp):
        if index>=len(cost):
            return 0
        if index==len(cost)-1:
            dp[index]=cost[-1]
            return cost[-1]
        if dp[index]!=-1:
            return dp[index]
        call1=cost[index]+self.solve1(index+1,cost,dp)
        call2=cost[index]+self.solve1(index+2,cost,dp)
        mini=min(call1,call2)
        dp[index]=mini
        return mini
    
    # tabulation
    def solve(self,index,cost,dp):
        n=len(cost)
        dp[n-1]=cost[-1]
        for j in range(n-2,-1,-1):
            mini=inf
            if j+1<=n-1:
                mini=min(mini,cost[j]+dp[j+1])
            else:
                mini=min(mini,cost[j])
            if j+2<=n-1:
                mini=min(mini,cost[j]+dp[j+2])
            else:
                mini=min(mini,cost[j])
            dp[j]=mini
        return min(dp[0],dp[1])
    
    #space optimization
    def solve(self,index,cost):
        n=len(cost)
        prev2=-1
        prev1=cost[-1]
        for j in range(n-2,-1,-1):
            mini=inf
            if prev1!=-1:
                mini=min(mini,prev1+cost[j])
            else:
                mini=min(mini,cost[j])
            if prev2!=-1:
                mini=min(mini,prev2+cost[j])
            else:
                mini=min(mini,cost[j])
            curr=mini
            prev2=prev1
            prev1=curr
        return min(prev1,prev2)
            
            
    

    



    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min(self.solve(0,cost),self.solve(1,cost))
        dp=[-1 for i in range(len(cost))]
        return self.solve(0,cost)
        
