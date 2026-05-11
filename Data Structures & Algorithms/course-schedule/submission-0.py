class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_reqs = {i: [] for i in range(numCourses)}
        for c in prerequisites:
            course = c[0]
            prereq = c[1]

            if course not in pre_reqs:
                pre_reqs[course] = []
            
            pre_reqs[course].append(prereq)
        
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False 
            elif pre_reqs[course] == []:
                return True

            visitSet.add(course)
            for prereq in pre_reqs[course]:
                if not dfs(prereq):
                    return False 
            visitSet.remove(course)
                
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return False 
            
        return True 
        