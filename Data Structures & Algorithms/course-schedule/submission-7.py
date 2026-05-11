class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list construction 
        # {course: prereqs}

        adjList = {i: set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].add(prereq)


        visited = set() 

        def dfs(course):
            if course in visited:
                return False 
            

            visited.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False 
            
            visited.remove(course)

            return True 
        

        # invoke our search relevant courses 
        for i in range(numCourses):
            if not dfs(i):
                return False 
        
        return True 



