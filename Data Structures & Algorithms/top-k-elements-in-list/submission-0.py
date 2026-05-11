class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapping = {} 
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        

        result = sorted(mapping.items(), key=lambda x: -x[1])

        return [val[0] for val in result[:k]]