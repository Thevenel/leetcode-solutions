class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map = {}
        
        # Count the frequency of each element in nums
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        # Sort the elements based on their frequency in descending order
        
        sorted_elements = sorted(frequency_map, key=frequency_map.get, reverse=True)
        
        # Return the top k frequent elements
        return sorted_elements[:k]