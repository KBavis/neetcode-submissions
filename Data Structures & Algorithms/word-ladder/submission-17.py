class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord == beginWord:
            return 0 
        elif endWord not in wordList:
            return 0

        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                postfix = word[i + 1: ] if i + 1 < len(word) else ""
                curr_pattern = word[:i] + "*" + postfix
                pattern_to_words[curr_pattern].append(word)
        


        q = deque([beginWord])
        curr_level = 1 
        seen = {beginWord}


        while q:
            curr_len = len(q)
            for i in range(curr_len):

                curr_word = q.popleft() 
                if curr_word == endWord:
                    return curr_level 
                

                # process neighbors
                for i in range(len(curr_word)):
                    postfix = curr_word[i + 1: ] if i + 1 < len(curr_word) else ""
                    curr_pattern = curr_word[:i] + "*" + postfix

                    for word in pattern_to_words[curr_pattern]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
                    
                    pattern_to_words[curr_pattern] = []
            
            curr_level += 1



        return 0
        

            
