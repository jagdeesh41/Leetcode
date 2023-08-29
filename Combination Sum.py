# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

class Solution:
    ans=[]
    #method 1
    def solve(self,index,candidates,target,l):
        if target<0:
            return
        if target==0:
            self.ans.append(l.copy())
            return
        for j in range(index,len(candidates)):
            self.solve(j,candidates,target-candidates[j],l+[candidates[j]])
    #method 2
    def solve(self,index,candidates,target,l):
        if target<0:
            return
        if index==len(candidates):
            if target==0:
                self.ans.append(l.copy())
            return
        pick=self.solve(index,candidates,target-candidates[index],l+[candidates[index]])
        skip=self.solve(index+1,candidates,target,l)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        self.ans=[]
        self.solve(0,candidates,target,l)
        return self.ans

        
        
