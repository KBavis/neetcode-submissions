class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        mapping = {}

        for i in range(len(numbers)):
            num = numbers[i]

            if target - num in mapping:
                return [mapping[target - num], i + 1]
            
            mapping[num] = i + 1
        

        return -1