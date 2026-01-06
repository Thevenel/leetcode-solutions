class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        
        for s in strs:
            count = [0] * 26  # There are 26 letters in the English alphabet
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)  # Use the count list as a key (tuples are hashable)
            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]

        return list(anagram_map.values())