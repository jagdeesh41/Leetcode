# 77. Combinations
# https://leetcode.com/problems/combinations/

class Solution:
    ans=[]
    #method 1
    def solve(self,count,k,l,n,prev):
        if count==k:
            self.ans.append(l.copy())
            return 
        if count==0:
            for choice in range(1,n+1):
                self.solve(count+1,k,l+[choice],n,choice)
        else:
            start=prev
            for choice in range(start+1,n+1):
                self.solve(count+1,k,l+[choice],n,choice)

  
    #method 2
    def solve(self,count,k,l,n):
        if count==k:
            self.ans.append(l.copy())
            return 
        if count==0:
            for choice in range(1,n+1):
                self.solve(count+1,k,l+[choice],n)
        else:
            start=l[-1]
            for choice in range(start+1,n+1):
                self.solve(count+1,k,l+[choice],n)
            
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans=[]
        l=[]
        self.solve(0,k,l,n)
        return self.ans


        
