class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {i: set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].add(prereq)
        

        visited = {i: 0 for i in range(numCourses)}
        res = [] 

        def dfs(course):
            
            if visited[course] == 2:
                return True
            elif visited[course] == 1:
                return False
            
            visited[course] = 1

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False 

            visited[course] = 2
            
            res.append(course)
            return True 

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        

