class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            Need to transform beginWord to endWord 

            Need to do it minimum ways possible 

            Need an easy way to determine "what candidates this current word can transform into"

            Using patterns to do so:
                *at: [bat, sat, cat]
            
            BFS sort of appraoch: 
                with only 1 transformation, what are the words I can change this into 
        """

        # determine if possible 
        if endWord not in wordList:
            return 0

        # setup pattern strucutre 
        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                postfix = word[i + 1:] if i + 1 < len(word) else ""
                pattern = word[:i] + "*" + postfix 
                pattern_to_words[pattern].append(word)
        

        # try transforming 
        q = deque([beginWord])
        visited = set()
        num_transformations = 1
        while q:

            curr_length = len(q)
            for i in range(curr_length):
                
                curr_word = q.popleft() 

                # ensure word hasn't been processed before
                if curr_word in visited:
                    continue 
                
                # check if we found our word 
                if curr_word == endWord:
                    return num_transformations
                
                # ensure it's marked as seen
                visited.add(curr_word)

                # account for words that we can transform curr_word into 
                for j in range(len(curr_word)):
                    postfix = curr_word[j + 1:] if j + 1 < len(curr_word) else ""
                    pattern = curr_word[:j] + "*" + postfix 
                    
                    for nei in pattern_to_words[pattern]:
                        if nei not in visited:
                            print(f"Appending Neighbor: {nei}")
                            q.append(nei)
            

            num_transformations += 1 
        
        return 0

            

            # consider words that this word can transform into 

        