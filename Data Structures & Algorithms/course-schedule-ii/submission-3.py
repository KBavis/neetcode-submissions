class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            [a, b] --> indicates you must take course a BEFORE course b 

            GOAL --> return any valid ordering of courses 

            1) setup an adj list 
                --> v --> [list, of, pre, reqs]

            2) create dfs function 
                    - should append to our res AFTER processing all pre-reqs 
                    - shouold densure that we have no cycles 

            3) iterate from [0, numCourses - 1] and call dfs 
        """


        adjList = {i: [] for i in range(numCourses)}
        for prereq in prerequisites: 
            adjList[prereq[0]].append(prereq[1])
        
        # setup visited dictionary as currently all not visited 
        visited = {i: 0 for i in range(numCourses)}

        self.res = []

        def dfs(course):
            if visited[course] == 2:
                return True 
            elif visited[course] == 1:
                return False 

            # mark course as currently visiting 
            visited[course] = 1

            for nei in adjList[course]:
                # cycle detected
                if not dfs(nei):
                    return False 
            
            # course completely processed 
            visited[course] = 2 

            # only add to res once completely processed 
            self.res.append(course)
            return True 
        

        # itereate through courses 
        for course in range(numCourses):
            if not dfs(course):
                return [] 
        
        return self.res 
            
