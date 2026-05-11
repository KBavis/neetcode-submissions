class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        prereqs = {i: [] for i in range(numCourses)}
        for p in prerequisites:
            course = p[0]
            pre = p[1]

            prereqs[course].append(pre)
        

        visited = set() 

        def dfs(course):
            if prereqs[course] == []:
                return True 
            elif course in visited:
                return False 
            
            visited.add(course)

            for pre in prereqs[course]:
                if not dfs(pre):
                    return False 
            
            visited.remove(course)
            return True 
        

        for course in range(numCourses):
            if not dfs(course):
                return False 
        
        return True 
        


        