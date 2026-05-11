class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list construction 
        # {course: prereqs}

        adjList = {i: set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].add(prereq)


        visited = {i: 0 for i in range(numCourses)}

        def dfs(course):
            if visited[course] == 1:
                return False
            elif visited[course] == 2:
                return True
            

            visited[course] = 1

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False 
            
            visited[course] = 2

            return True 
        

        # invoke our search relevant courses 
        for i in range(numCourses):
            if not dfs(i):
                return False 
        
        return True 



