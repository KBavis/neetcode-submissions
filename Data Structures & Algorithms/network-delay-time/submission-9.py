class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            Directed Graph where we are able to start from anywhere 

            Brute Force would be something like this:
                Start at Node k: 
                    --> determine neighbors
                    --> transverse to one of neighbors 
                    --> continue down this path and record minimum times 
                    --> backtrack sort of approach where we need to recurse down many paths and record minimimum
                
                DFS Brute Force Time Complexity:
                    at each node: we have 4 (technically three paths)
                    memoization though so we can at least reduce in this way 
                    O(work per each state * number of states)
                        n * n --> O(n^2)

            
            Optimized Solution (BFS):
                --> setup adjancy list: node: [neighbors]
                --> start at current node (initi queue with 0 cost)
                    --> if this node has been seen previously, skip
                    --> if not, add the cost to our total 
                -->  find neighbors to node K
                        --> add these to queue 
                -->  greedily always choose the "smallest" cost path to navigate to the next node 
                        --> we can enforce this by having our "queue" just be a min heap 
                --> continue while queue isn't empty and len(visited) != n 
        """



        adjList = {i: [] for i in range(1, n + 1)}
        for source, target, cost in times:
            adjList[source].append((cost, target))

        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            
            # ensure that we're greedily grabbing cheapest of neighbors to travel to 
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue 
            
            # account for node being seen
            visited.add(curr_node)

            if len(visited) == n:
                return curr_cost

            # account for neighbors 
            for nei_cost, nei_node in adjList[curr_node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_cost + curr_cost, nei_node))
            
        

        return -1