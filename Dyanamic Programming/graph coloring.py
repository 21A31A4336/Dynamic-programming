graph=[[10,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
def issafe(vertex,colo,t):
    for i in range(t):
        if graph[vertex][i]==1 and color[i]==colo:
            return False
    return True
def play(color,n,ver,t):
    if ver==t:
        print(color)
        return True
    for col in range(1,n+1):
        if issafe(ver,color,t):
            color[ver]=col
            if play(color,n,ver+1,t):
                return True
            color[ver]=0
    return False
n=3
color=[0]*len(graph)
play(color,n,0,len(graph))