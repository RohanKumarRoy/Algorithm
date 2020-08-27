# find cycle in undirected graph using union and find algorithm.
def find(v):
    if parent[v]==-1:
        return v
    return find(parent[v])

def union(fromP,toP):
    fromP,toP=find(fromP),find(toP)
    parent[fromP]=toP


def isCycle(adjList):
    for u,v in adjList:
        fromP,toP=find(u),find(v) #find absolute parent
        if fromP==toP:
            return "Cycle"
        union(fromP,toP) #if absolute parent are not same then do union
    return "No Cycle"

no_of_edge=int(input())
no_of_vertex=int(input())
parent=[-1]*no_of_vertex
adjList=[]
for edge in range(no_of_edge):
    u,v=map(int,input().split())
    adjList.append([u,v])
print(isCycle(adjList))
# time complexity=O(E*V)

