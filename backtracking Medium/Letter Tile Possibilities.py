# 1079. Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def solve(self,count,tiles,visited,l):
        cnt=0
        taken=set()
        for index in range(0,len(tiles)):
            if visited[index]==0 and tiles[index] not in taken:
                visited[index]=1
                taken.add(tiles[index])
                pick=self.solve(count+1,tiles,visited,l+tiles[index])
                cnt+=pick
                visited[index]=0
        return cnt+1
        


    def numTilePossibilities(self, tiles: str) -> int:
        visited=[0 for i in range(len(tiles))]
        l=""
        """
        As [] is not a permutation on the root node its l+r but not l+r+1 as [] is not 
        considered so return must be 1 less than total 
        """
        return self.solve(0,tiles,visited,l)-1
        
