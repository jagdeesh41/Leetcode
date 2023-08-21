class Solution:
    ans=[]
    def solve(self,index,graph,l):
        if index==len(graph)-1:
            l+=[index]
            self.ans.append(l.copy())
            return
        for i in graph[index]:
            pick=self.solve(i,graph,l+[index])
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans=[]
        l=[]
        self.solve(0,graph,l)
        return self.ans

