
# detect cycle in undirected graph using bfs

def checkCycle(adjList,visited,curr):
    if visited[curr]:
        return True
    visited[curr]=True
    flag=False
    for i in range(len(adjList[curr])):
        flag=checkCycle(adjList,visited,adjList[curr][i])
        if flag:
            return True
    return False

def isCycle(n,adjList):
    visited=[False]*n
    for i in range(n):
        visited[i]=True        
        for j in range(len(adjList[i])):
            found=checkCycle(adjList,visited,adjList[i][j])
            if found:
                return True
        visited[i]=False
    return False

adjList={}
adjList[0]=[1]
adjList[1]=[]
adjList[2]=[1,3]
adjList[3]=[4]
adjList[4]=[0,2]
print(isCycle(5,adjList))
