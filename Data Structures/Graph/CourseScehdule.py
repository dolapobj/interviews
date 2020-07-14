#Course Schedule 
#LC 207 

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 
you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, 
             and to take course 0 you should
             also have finished course 1. So it is impossible.

"""
#note --> graph is represented by list of edges
#idea: check if directed graph is acyclic
    #each vertex can have three states, 
    #0--> not visited
    #-1 --> currently being processed in call stack 
    #1--> vertex and its descendants are procvessed
def canFinish(numCourses,prereqs):
    graph = buildGraph(numCourses,prereqs)
    state = [0]*numCourses
    def hasCycle(v):
        if state[v] ==1:
            #already processed 
            return False 
        if state[v] ==-1:
            return True 
        state[v] = -1
        for i in graph[v]:
            if hasCycle(i):
                return True
        state[v] = 1
        return False
    for v in range(numCourses):
        if hasCycle(v):
            return False 
    return True 
def buildGraph(numCourses,prereqs):
    graph = [[] for i in range(numCourses)]
    for c1,c2 in prereqs:
        graph[c2].append(c1)
    return graph

#RT: O(V+E) 
#SC: O(V+E) --> adjacency list representation of graph