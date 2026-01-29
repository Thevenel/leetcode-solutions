class Solution:
    def __init__(self):
        self.store = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Example usage:
kv = Solution()
kv.set("foo", "bar", 1)
print(kv.get("foo", 1))  # Output: "bar"
print(kv.get("foo", 3))  # Output: "bar"
kv.set("foo", "bar2", 4)
print(kv.get("foo", 4))  # Output: "bar2"
print(kv.get("foo", 5))  # Output: "bar2"

