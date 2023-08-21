# 2375. Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    ans=0
    def solve(self,index,pattern,num,visited):
        if index==len(pattern):
            self.ans=str(num)
            return True
        if pattern[index]=="I":
            #increase 
            ld=num%10
            for choice in range(ld+1,10):
                if visited[choice]==0:
                    visited[choice]=1
                    if self.solve(index+1,pattern,num*10+choice,visited):
                        return True
                    visited[choice]=0
        else:
            #decrease
            ld=num%10
            for choice in range(ld-1,0,-1):
                if visited[choice]==0:
                    visited[choice]=1
                    if self.solve(index+1,pattern,num*10+choice,visited):
                        return True
                    visited[choice]=0
            


    def smallestNumber(self, pattern: str) -> str:
        self.ans=0
        for num in range(1,10):
            visited=[0 for i in range(10)]
            visited[num]=1
            if self.solve(0,pattern,num,visited):
                return self.ans

        