# recursive
def solve1(index,heights,k):
    if index==len(heights)-1:
        return 0
    mini=float('inf')
    for step in range(1,k+1):
        if index+step<=len(heights)-1:
            mini=min(mini,abs(heights[index]-heights[index+step])+solve1(index+step,heights,k))
    return mini
# memoization
def solve2(index,heights,k,dp):
    if index==len(heights)-1:
        return 0
    if dp[index]!=-1:
        return dp[index]
    mini=float('inf')
    for step in range(1,k+1):
        if index+step<=len(heights)-1:
            mini=min(mini,abs(heights[index]-heights[index+step])+solve2(index+step,heights,k,dp))
    dp[index]=mini
    return mini

#tabulation
def solve(index,heights,k,dp):
    n=len(heights)
    dp[n-1]=0
    for j in range(n-2,-1,-1):
        mini=float('inf')
        for step in range(1,k+1):
            if j+step<=n-1:
                mini=min(mini,abs(heights[j]-heights[j+step])+dp[j+step])
        dp[j]=mini
    return dp[0]
                
                
                
        

n,k=map(int,input().split())
heights=list(map(int,input().split()))
dp=[-1 for i in range(n+1)]
print(solve(0,heights,k,dp))
