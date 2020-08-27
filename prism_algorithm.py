inf=10**9
from collections import defaultdict
def findMin(value,setMST):
    min=inf
    vertex=0
    for i in range(len(value)):
        if setMST[i]==False and value[i]<min:
            min=value[i]
            vertex=i
    return vertex

def PrismAlgorithm(adjMatrix,v):
    value=[inf]*v #to store cost
    value[0]=0
    setMST=[False]*v #visited node
    parent=[-1]*v #parent node to get the path
    for i in range(v):
        u=findMin(value,setMST)
        setMST[u]=True
        for j in range(v):
            if adjMatrix[u][j]!=0 and value[j]>adjMatrix[u][j] and setMST[j]==False:
                value[j]=adjMatrix[u][j]
                parent[j]=u
    path=defaultdict(list)
    for i in range(v):
        for j in range(v):
            if parent[j]==i:
                path[i].append(j)
    for source in path:
        dest=path[source]
        for x in dest:
            print(source,"-->",x,value[x])

adjMatrix=[ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
PrismAlgorithm(adjMatrix,len(adjMatrix))
#TC (V^2)
