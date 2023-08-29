#401. Binary Watch
#https://leetcode.com/problems/binary-watch/

class Solution:
    ans=[]
    def solve(self,index,time,l,count,on,mins,hrs):
        if count==on:
            if mins<60 and hrs<12:
                self.ans.append(str(hrs)+":"+str(mins).zfill(2))
            return
        if index==len(time):
            return
        if 0<=index<=5:
            mins+=time[index]
            pick=self.solve(index+1,time,l+[time[index]],count+1,on,mins,hrs)
            mins-=time[index]
        elif index>5:
            hrs+=time[index]
            pick=self.solve(index+1,time,l+[time[index]],count+1,on,mins,hrs)
            hrs-=time[index]
        np=self.solve(index+1,time,l,count,on,mins,hrs)

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.ans=[]
        time=[1,2,4,8,16,32,1,2,4,8]
        l=[]
        hrs=0
        mins=0
        self.solve(0,time,l,0,turnedOn,hrs,mins)
        return self.ans


        
