# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    ans=[]
    def solve(self,index,s,n_s):
        if index==len(s):
            self.ans.append(n_s)
            return
        if ord('0')<=ord(s[index])<=ord('9'):
            pick_digit=self.solve(index+1,s,n_s+s[index])
        elif ord('a')<=ord(s[index])<=ord('z') or ord('A')<=ord(s[index])<=ord('Z'):
            pick_lower=self.solve(index+1,s,n_s+s[index].lower())
            pick_upper=self.solve(index+1,s,n_s+s[index].upper())


        
        
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans=[]
        n_s=""
        self.solve(0,s,n_s)
        return self.ans

        