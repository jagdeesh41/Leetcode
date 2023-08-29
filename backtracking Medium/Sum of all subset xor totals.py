# 1863. Sum of All Subset XOR Totals
#https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def solve(self,index,nums,l,tot_xor):
        if index==len(nums):
            return tot_xor
        pick=self.solve(index+1,nums,l+[nums[index]],tot_xor^nums[index])
        np=self.solve(index+1,nums,l,tot_xor)
        return pick+np

    def subsetXORSum(self, nums: List[int]) -> int:
        l=[]
        tot_xor=0
        return self.solve(0,nums,l,tot_xor)
        
