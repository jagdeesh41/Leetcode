
"""
Given an m x n grid of characters board and a string word, return true
if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
word = "ABCCED"
Output: true
Input: board =
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]],
word = "SEE"
Output: true
"""


def search(row,col,board,m,n,word,index,path,temp):
    if index==len(word)-1:
        return True
    flag=False
    store=board[row][col]
    board[row][col]="$"
    for dir in range(4):
        n_r=row+temp[dir][0]
        n_c=col+temp[dir][1]
        index+=1
        if n_r>=0 and n_c>=0 and n_r<m and n_c<n and index<len(word) and board[n_r][n_c]==word[index]:
            if search(n_r,n_c,board,m,n,word,index,path+word[index],temp):
                return True
        index-=1
    board[row][col]=store
    return False


def exist(board, word):
    m=len(board)
    n=len(board[0])
    d=set()
    for i in range(m):
        for j in range(n):
            d.add(board[i][j])
    for i in word:
        if i not in d:
            return False
    index=0
    path=""
    flag=False
    temp=[[-1,0,"T"],[0,-1,"L"],[0,1,"R"],[1,0,"B"]]
    for i in range(m):
        for j in range(n):
            if board[i][j]==word[index]:
                if search(i,j,board,m,n,word,index,path,temp):
                    return True
    return False
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))

    
