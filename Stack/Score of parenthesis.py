# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        st=[]
        for i in range(len(s)):
            if st==[]:
                st.append(s[i])
            elif st and st[-1]!="(" and s[i]==")":
                tot=0
                while(st[-1]!="("):
                    tot+=st[-1]
                    st.pop()
                st.pop()
                st.append(2*tot)
            elif st and st[-1]=="(" and s[i]==")":
                st.pop()
                st.append(1)
            else:
                st.append(s[i])
        return sum(st)
        
