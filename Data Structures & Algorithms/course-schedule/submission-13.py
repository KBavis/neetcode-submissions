class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] will be written as a --> b, meaning a depends on b 


        adjList = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:

            adjList[prereq].append(course)
        
        visited = {i: 0 for i in range(numCourses)}

        def dfs(course):
            if visited[course] == 1:
                return False 
            elif visited[course] == 2:
                return True 
            

            visited[course] = 1 
            for nei in adjList[course]:
                if not dfs(nei):
                    return False 
            

            visited[course] = 2 
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False 
        
        return True 
