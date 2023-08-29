# 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    mini=inf
    def solve(self,index,cookies,k,bucket):
        if index==len(cookies):
            self.mini=min(self.mini,max(bucket))
            return
        
        for choice in range(len(bucket)):
            if bucket[choice]+cookies[index]>=self.mini:
                continue
            bucket[choice]+=cookies[index]
            self.solve(index+1,cookies,k,bucket)
            bucket[choice]-=cookies[index]
            if bucket[choice]==0:
                return
        

    def distributeCookies(self, cookies: List[int], k: int) -> int:

        bucket=[0 for i in range(k)]
        self.solve(0,cookies,k,bucket)
        return self.mini


        
