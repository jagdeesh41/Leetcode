#78. Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    ans=[]
    def solve1(self,index,nums,l):
        if index==len(nums):
            self.ans.append(l[:])
            return
        pick=self.solve1(index+1,nums,l+[nums[index]])
        np=self.solve(index+1,nums,l)

    def solve2(self,index,nums,l):
        for j in range(index,len(nums)):
            self.solve2(j+1,nums,l+[nums[j]])
        """"
        goes till to the depth and then to the nodes where the childs in the depth are already done
        going to the depth means visiting the leaf first and completing all the calls and coming from leaf to the root
        For every dfs problem we can start doing things after the recursion calls 
        start writing conditions in the backtracking 
        """
        self.ans.append(l.copy())
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        l=[]
        self.solve2(0,nums,l)
        return self.ans

        