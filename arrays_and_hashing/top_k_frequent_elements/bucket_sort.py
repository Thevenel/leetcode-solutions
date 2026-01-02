class Solution:
    def topkFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Frequency Mapping
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # Step 2: Bucket Creation
        max_freq = max(frequency_map.values())
        buckets = [[] for _ in range(max_freq + 1)]
        
        for num, freq in frequency_map.items():
            buckets[freq].append(num)
        
        # Step 3: Collecting Top K Frequent Elements
        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result