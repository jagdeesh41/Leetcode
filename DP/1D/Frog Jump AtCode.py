# A - Frog 1
# https://atcoder.jp/contests/dp/tasks


#recursion
def solve(index,heights):
    if index==len(heights)-1:
        return 0
    mini=inf
    mini=min(mini,abs(heights[index+1]-heights[index])+solve(index+1,heights))
    if index+2<=len(heights)-1:
        mini=min(mini,abs(heights[index]-heights[index+2])+solve(index+2,heights))
    return mini

# memoization
def solve(index,heights,dp):
    if index==len(heights)-1:
        return 0
    if dp[index]!=-1:
        return dp[index]
    mini=inf
    mini=min(mini,abs(heights[index+1]-heights[index])+solve(index+1,heights,dp))
    if index+2<=len(heights)-1:
        mini=min(mini,abs(heights[index]-heights[index+2])+solve(index+2,heights,dp))
    dp[index]=mini
    return mini
  
# tabulation
def solve(index,heights,dp):
    n=len(heights)
    dp[n-1]=0
    for j in range(n-2,-1,-1):
        mini=dp[j+1]+abs(heights[j+1]-heights[j])
        if j+2<=n-1:
            mini=min(mini,dp[j+2]+abs(heights[j+2]-heights[j]))
        dp[j]=mini 
    return dp[0]

#space optimization
def solve(index,heights,dp):
    n=len(heights)
    prev1=0
    prev2=-1
    for j in range(n-2,-1,-1):
        mini=prev1+abs(heights[j+1]-heights[j])
        if prev2!=-1:
            mini=min(mini,prev2+abs(heights[j+2]-heights[j]))
        prev2=prev1
        prev1=mini 
    return prev1




def frogJump(n: int, heights: List[int]) -> int:
    dp=[-1 for i in range(len(heights))]
    return solve(0,heights,dp)
    
    
