class Solution:
    ans=""
    def solve(self,index,arr,count,hrs,mins,visited):
        if hrs>23:
            return False
        if mins>59:
            return False
        if count==4:
            self.ans=str(hrs).zfill(2)+":"+str(mins).zfill(2)
            return True
        if count<2:
            #conditions for minutes
            for j in range(0,len(arr)):
                if visited[j]==0:
                    visited[j]=1
                    l_d=arr[j]
                    new_hrs=(hrs*10)+l_d
                    if self.solve(j+1,arr,count+1,new_hrs,mins,visited):
                        return True
                    visited[j]=0

        if count>=2:
            #condition for seconds
            for j in range(0,len(arr)):
                if visited[j]==0:
                    visited[j]=1
                    l_d=arr[j]
                    new_mins=(mins*10)+l_d
                    if self.solve(j+1,arr,count+1,hrs,new_mins,visited):
                        return True
                    visited[j]=0
        return False
  
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        self.ans=""
        visited=[0 for i in range(len(arr))]
        self.solve(0,arr,0,0,0,visited)
        return self.ans
