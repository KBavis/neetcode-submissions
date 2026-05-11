class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = [] 

        def search(s, soFar, idx):

            if idx == len(s):
                res.append(list(soFar))
                return 
            

            for i in range(idx, len(s)):
                
                # construct current word and relevant pointers
                currWord = s[idx : i + 1]
                mid = len(currWord) // 2 
                right = mid + 1 if len(currWord) % 2 != 0 else mid
                
                # check if the current word is a palindrome
                if isPalindrome(currWord, mid - 1, right):

                    soFar.append(currWord)
                    search(s, soFar, i + 1)
                    soFar.pop() 
        

        def isPalindrome(s, left, right):
            if not s:
                return False 
            

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 
                right += 1 
            

            return left == -1 and right == len(s)
    


        search(s, [], 0)

        return res 



