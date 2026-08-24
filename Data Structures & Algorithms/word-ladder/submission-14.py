class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            a) conveinient way to determine if we can transform a word into another word:
                    cat --> [set of words cat can transform into]
            

            b) prioritize smallest distnaces from the current word 

            pattern --> words that fit that pattern 

            don't want to transverse back to a word we already transformed into if possible 
        """

        pattern_to_words = defaultdict(list)

        for word in wordList:
            
            # setup pattern to corresponding word 
            for i in range(len(word)):
                postfix = word[i + 1: ] if i + 1 < len(word) else ""
                curr_pattern = word[:i] + "*" + postfix 
                pattern_to_words[curr_pattern].append(word)

        print(pattern_to_words)
        
        # [cat, 0], {cat}
        # [(bat, 1)], {cat, bat}
        # [(bag, 2)], {cat, bat, bag}
        # [(sag, 3), (dag, 3)]

        if endWord not in wordList:
            return 0
        elif beginWord == endWord:
            return 0

        q = deque([beginWord])
        seen = {beginWord}
        num_changes = 1 

        while q:

            current_level = len(q)
            for i in range(current_level):

                curr_word = q.popleft() 
                if curr_word == endWord:
                    return num_changes
                

                # process neighbors (1 transformation only)
                for i in range(len(curr_word)):
                    postfix = curr_word[i + 1: ] if i + 1 < len(curr_word) else ""
                    curr_pattern = curr_word[:i] + "*" + postfix 
                    
                    for word in pattern_to_words[curr_pattern]:
                        if word not in seen:
                            seen.add(word)
                            q.append(word)
            
            print(f"State of Queue After Level={num_changes} --> {q}")
            num_changes += 1 
        

        return 0

            


            
