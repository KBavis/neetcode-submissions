class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        low = 0 
        high = len(numbers) - 1

        while low < high:
            
            tmp = numbers[low] + numbers[high]

            if tmp == target:
                return [low + 1, high + 1]
            elif tmp > target:
                high -= 1
            else:
                low += 1 
        
        return []