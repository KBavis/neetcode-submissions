class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True 
        
        adjList = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        

        visited = set() 

        def dfs(course):
            if course in visited:
                return False 
            
            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False 
                
            visited.remove(course)
            return True 
        


        for course in range(numCourses):
            if not dfs(course):
                return False 
        
        return True 


        


