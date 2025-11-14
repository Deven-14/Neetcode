class MyHashMap:

    def __init__(self):
        self.prime = 1007
        self.keys = [[] for _ in range(self.prime)]
        self.values = [[] for _ in range(self.prime)]
    
    def _hash(self, key) -> int:
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        try:
            idx = self.keys[hash_key].index(key)
            self.values[hash_key][idx] = value
        except ValueError:
            self.keys[hash_key].append(key)
            self.values[hash_key].append(value)
        
    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        try:
            idx = self.keys[hash_key].index(key)
        except ValueError:
            return -1
        
        return self.values[hash_key][idx]

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        try:
            idx = self.keys[hash_key].index(key)
            self.keys[hash_key].pop(idx)
            self.values[hash_key].pop(idx)
        except ValueError:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)