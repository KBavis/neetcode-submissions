class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        

        visited = set() 

        def dfs(course):
            if course in visited:
                return False 


            visited.add(course)

            for nei in adjList[course]:     
                if not dfs(nei):
                    return False 
            

            visited.remove(course)

            return True 
        

        for course in range(numCourses):
            if not dfs(course):
                return False 
        

        return True 

