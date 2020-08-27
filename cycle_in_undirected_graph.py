# detect cycle in undirected graph using graph coloring

def checkCycle(adjList,visited,curr):
    if visited[curr]==2:
        return True
    visited[curr]=1
    for i in range(len(adjList[curr])):
        if visited[adjList[curr][i]]==1:
            visited[adjList[curr][i]]=2
        else:
            found=checkCycle(adjList,visited,adjList[curr][i])
            if found:
                return True
    return False

def isCycle(n,adjList):
    visited=[0]*n
    for i in range(n):
        visited[i]=1
        for j in range(len(adjList[i])):
            found=checkCycle(adjList,visited,adjList[i][j])
            if found:
                print(visited)
                return True
        visited[i]=0
    print(visited)
    return False

adjList={}
adjList[0]=[1,2]
adjList[1]=[0]
adjList[2]=[0,3]
print(isCycle(3,adjList))
