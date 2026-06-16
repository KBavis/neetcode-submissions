class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            a) Goal is to transform the begin word to endWord via the words in the wordList 
                    --> if end word not in wordList, return 0
            
            b) Need to setup an easy way to determine if you can transform a word into another word:
                    pattern: [list of words]
                    *at: [cat, bat, sat]
            
            c) We then should iterate through our options of words to iterate through, and reurse down that path 
                 - likely some optimizations we can make? 
                 - need a count of current transformations 
                 - need a min transformations 
                 - if we ever exceed the min transformations then we should terminate early
        """

        # early termination 
        if endWord not in wordList:
            return 0

        # add begin word to wordList 
        wordList.append(beginWord)

        # generate patterns 
        patterns = defaultdict(list)
        for word in wordList:
            
            for i in range(len(word)):
                pre_word = word[:i]
                post_word = word[i + 1:] if i + 1 < len(word) else ""

                curr_pattern = pre_word + "*" + post_word 
                patterns[curr_pattern].append(word)
        
        # start BFS transversal 
        min_transformations = float('inf')
        curr_words = 1

        q = deque([beginWord])
        seen_words = {beginWord}

        while q:

            # determine current level length 
            length = len(q)

            # iterate through only current level 
            for i in range(length):

                # extract current word to process 
                word = q.popleft() 
                if word == endWord:
                    return curr_words 
                

                # process neighbors 
                for i in range(len(word)):
                    pre_word = word[:i]
                    post_word = word[i + 1:] if i + 1 < len(word) else ""
                    curr_pattern = pre_word + "*" + post_word 

                    # extract potential candidates to process 
                    for candidate in patterns[curr_pattern]:

                        # ensure no duplicate candidates are processed 
                        if candidate not in seen_words:
                            q.append(candidate)
                            seen_words.add(candidate)
            

            # increment the current number of words 
            curr_words += 1 
        
        # end word not found 
        return 0