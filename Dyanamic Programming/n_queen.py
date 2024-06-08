def issafe(board,i,j,n):
    orgi=i
    orgj=j
    for col in range(n):
        if board[i][col]==1:
            return False
    for rows in range(n):
        if board[rows][j]==1:
            return False
    while i>=0 and i<n and j>0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
        i=orgi
        j=orgj
    while i>=0 and i<n and j>0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    return True
def play(board,row,col,n):
    if row==n:
        for i in board:
            print(i,' ')
        exit()
    for i in range(col):
        if issafe(board,row,i,n):
            board[row][i]=1
            play(board,row+1,col,n)
            board[row][i]=0
n=int(input("queens?"))
board=[[0]*n for i in range(n)]
play(board,0,n,n)