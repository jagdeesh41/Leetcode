# 1286. Iterator for Combination
# https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator:

    ans=[]
    i=0
    def solve1(self,index,count,c,length,n_s):
        if count==length:
            self.ans.append(n_s)
            return
        if index==len(c):
            return
        pick=self.solve1(index+1,count+1,c,length,n_s+c[index])
        np=self.solve1(index+1,count,c,length,n_s)

    def solve2(self,index,count,c,length,n_s):
        if count==length:
            self.ans.append(n_s)
            return
        for j in range(index,len(c)):
            self.solve2(j+1,count+1,c,length,n_s+c[j])

    def __init__(self, c: str, length: int):
        self.ans=[]
        self.i=0
        self.solve2(0,0,c,length,"")

        

    def next(self) -> str:
        temp=self.ans[self.i]
        self.i+=1
        return temp
        
        

    def hasNext(self) -> bool:
        return self.i<len(self.ans)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()