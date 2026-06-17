class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # setup adj list 
        adjList = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)
        

        # transverse
        visited = {i: 0 for i in range(numCourses)}
        def dfs(course):
            if visited[course] != 0:
                return visited[course] == 2
            

            visited[course] = 1 
            for nei in adjList[course]:
                if not dfs(nei):
                    return False 
            

            visited[course] = 2 
            return True 
        

        # call on each course 
        for i in range(numCourses):
            if not dfs(i):
                return False 
        

        return True 
