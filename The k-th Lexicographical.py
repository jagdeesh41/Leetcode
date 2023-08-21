# 1415. The k-th Lexicographical String of All Happy Strings of Length n
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    ans=0
    kth_str=""
    def solve(self,count,s,n_s,n,k):
        if count==n:
            self.ans+=1
            if self.ans==k:
                self.kth_str=n_s
                return True
            return False
        for j in "abc":
            if (len(n_s)>=1 and n_s[-1]!=j )or len(n_s)==0:
                if self.solve(count+1,s,n_s+j,n,k):
                    return True

    def getHappyString(self, n: int, k: int) -> str:
        self.ans=0
        self.kth_str=""
        s="abc"
        self.solve(0,s,"",n,k)
        return self.kth_str


        