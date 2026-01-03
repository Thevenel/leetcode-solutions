class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s  # append size of string followed by a '#'
        return res
    
    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            len_str = int(s[i:j])  # extract the length of the string
            j += 1  # move past the '#'
            res.append(s[j:j + len_str])  # extract the string of given length
            i = j + len_str  # move to the next size indicator
        return res

strs = ["hello", "world", "hi"]
csl = Solution()
encoded_str = csl.encode(strs)
print("Encoded string:", encoded_str)
decoded_strs = csl.decode(encoded_str)
print("Decoded strings:", decoded_strs)