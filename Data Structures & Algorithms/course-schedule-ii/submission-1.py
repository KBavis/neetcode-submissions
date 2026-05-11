class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            [a,b] ==> a --> b  ===> a is dependent on course b


            Post Order DFS and then returning our result in reverse order

            Unable to return solution if we detect a cycle 
        """


        adjList = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            adjList[c1].append(c2)
        
        
        # 0 = not seen, 1 = currently processing, 2 = Finished
        visited = {i: 0 for i in range(numCourses)} 
        res = []

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
            res.append(course) # post-order 
            return True 
        

        # call search on all courses 
        for course in range(numCourses):
            if not dfs(course):
                return [] 
        

        return res


