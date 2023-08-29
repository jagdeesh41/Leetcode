# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    ans=[]
    def solve(self,n,open,close,n_s):
        if close==open==n:
            self.ans.append(n_s)
            return
        if open>n:
            return
        if close>open:
            return
        
        self.solve(n,open+1,close,n_s+"(")
        self.solve(n,open,close+1,n_s+")")


    def generateParenthesis(self, n: int) -> List[str]:
        self.ans=[]
        self.solve(n,0,0,"")
        return self.ans



        
