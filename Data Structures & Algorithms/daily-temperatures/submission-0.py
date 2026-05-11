class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.bruteForce(temperatures)

    


    def bruteForce(self, temperatures):

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > curr_temp:
                    result[i] = j - i
                    break 
        
        return result 
