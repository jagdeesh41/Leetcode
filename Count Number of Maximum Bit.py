# 2044. Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution:
    def solve1(self,index,nums,curr_or,req_or):
        if index==len(nums):
            if curr_or==req_or:
                return 1
            return 0
        pick=self.solve1(index+1,nums,curr_or|nums[index],req_or)
        np=self.solve1(index+1,nums,curr_or,req_or)
        return pick+np
    
    def solve2(self,index,nums,curr_or,req_or):
        parent=curr_or
        cnt=0
        for j in range(index,len(nums)):
            cnt+=self.solve2(j+1,nums,curr_or|nums[j],req_or)
        """
        if leaf node then there is no for loop for it so its is the maximum depth of the tree 
        we calculate at leaf node as :
            from for loop we get no count and now WE CHECK NODE DATA IF IT IS MEETING THE CONDITION then change count to count+1 
        For non leaf node :
            The same process is done at non leaf node where we have for loop already handled the child data with return values
            so we have count ready and now check with the NODE DATA IF IT IS MEETING THE CONDITION then change count to count+1
        """
        if parent==req_or:
            return cnt+1
        return cnt




    def countMaxOrSubsets(self, nums: List[int]) -> int:
        req_or=0
        for i in nums:
            req_or|=i
        return self.solve1(0,nums,0,req_or)
        