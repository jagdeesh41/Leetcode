
"""
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. 
For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner,
sorted in lexicographical order.


Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]
"""
#method 1
s=input()
l=[]
flag=True
temp=""
for i in range(len(s)):
    if s[i]=="{":
        flag=False
    elif s[i]=="}":
        l.append(temp)
        temp=""
        flag=True
    elif s[i] and flag==True:
        l.append(s[i])
    elif flag==False:
        if s[i]!=",":
            temp+=s[i]
def solve(index,l,ans,n_s):
    if index==len(l):
        ans.append(n_s)
        return 
    for choice in sorted(l[index]):
        u_s=n_s+choice
        solve(index+1,l,ans,u_s)
ans=[]
solve(0,l,ans,"")
print(ans)


#method 2
s=input()
l=[]
def solve(index,s,n_s,ans):
    if index==len(s):
        ans.append(n_s)
        return 
    if s[index]=="{":
        start=index+1
        # find "}"
        end=s.index("}",index)
        temp=[]
        for ele in s[start:end].split(","):
            temp.append(ele)
        print(temp)
        for choice in sorted(temp):
            solve(end+1,s,n_s+choice,ans)
    else:
        solve(index+1,s,n_s+s[index],ans)
ans=[]
solve(0,s,"")
print(ans)
        
        
        
    
    




    
            

    
    
        
        
    
        
