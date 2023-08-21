class Solution:
    ans=[]
    def solve(self,nums,visited,l,count):
        if count==len(nums):
            self.ans.append(l.copy())
            return
        for choice in range(0,len(nums)):
            if visited[choice]==0:
                visited[choice]=1
                pick=self.solve(nums,visited,l+[nums[choice]],count+1)
                visited[choice]=0
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        visited=[0 for i in range(len(nums))]
        l=[]
        """
        we find permutations based on count not based on indexing as index always starts from 0

        Dont use index as paramter here.
        """
        self.solve(nums,visited,l,0)
        return self.ans
        