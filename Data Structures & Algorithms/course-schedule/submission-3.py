class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build adjacency list 
        adjList = {i: [] for i in range(numCourses)}
        for course in prerequisites:
            adjList[course[0]].append(course[1])
        
        visited = set()

        def dfs(course):
            if adjList[course] == []:
                return True 
            elif course in visited:
                return False 
            

            visited.add(course)

            for c in adjList[course]:
                if not dfs(c):
                    return False 
            

            visited.remove(course)

            return True 
        


        for course in range(numCourses):
            if not dfs(course):
                return False 
        
        return True 
            
