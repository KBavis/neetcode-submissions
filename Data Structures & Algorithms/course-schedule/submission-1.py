class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # mapping of courses to their pre-reqs 
        mapping = {i: [] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]

            mapping[course].append(prereq)

        visited = set()
        
        # dfs for determine if impossible 
        def dfs(prereq):
            if prereq in visited:
                return False

            prereqs = mapping[prereq]
            if prereqs == []:
                return True 
            
            visited.add(prereq)
            for p in prereqs:
                if not dfs(p):
                    return False 
            visited.remove(prereq)

            return True 
        

        for course in range(numCourses):
            if not dfs(course):
                return False 
        
        return True 
                 
            

        


