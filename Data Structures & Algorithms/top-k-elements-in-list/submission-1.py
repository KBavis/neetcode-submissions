class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # calculate frequency 
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        
        # extract result 
        sorted_tuples = sorted(mapping.items(), key=lambda x: x[1], reverse=True)
        result = [val[0] for val in sorted_tuples[:k]]
        return result 
        