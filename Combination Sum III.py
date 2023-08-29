# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    ans=[]
    def solve(self,index,k,target,arr,l):
        if k==0:
            if target==0:
                self.ans.append(l.copy())
            return
        if index==len(arr):
            return
        if target<0:
            return
        
        pick=self.solve(index+1,k-1,target-arr[index],arr,l+[arr[index]])
        skip=self.solve(index+1,k,target,arr,l)
    def solve(self,index,k,target,arr,l):
        if target<0:
            return
        if k==0:
            if target==0:
                self.ans.append(l.copy())
            return
        for j in range(index,len(arr)):
            self.solve(j+1,k-1,target-arr[j],arr,l+[arr[j]])
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l=[]
        self.ans=[]
        arr=[i for i in range(1,10)]
        self.solve(0,k,n,arr,l)
        return self.ans

        
