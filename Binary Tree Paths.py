# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=[]
    def solve(self,root,path):
        if root==None:
            return 
        if root.left==None and root.right==None:
            path+=str(root.val)
            self.ans.append(path)
            return
        left=self.solve(root.left,path+str(root.val)+"->")
        right=self.solve(root.right,path+str(root.val)+"->")
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans=[]
        self.solve(root,"")
        return self.ans



        
