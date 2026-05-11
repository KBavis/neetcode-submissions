class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        mapping = {}
        for i in range(len(numbers)):
            if target - numbers[i] in mapping:
                return [mapping[target - numbers[i]], i + 1]
            
            mapping[numbers[i]] = i + 1
        
        return None 