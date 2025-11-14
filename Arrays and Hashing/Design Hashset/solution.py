class MyHashSet:

    def __init__(self):
        self.prime = 1007
        self.collection = [[] for _ in range(self.prime)]
    
    def _hash(self, key) -> int:
        return key % self.prime

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        try:
            self.collection[hash_key].index(key)
        except ValueError:
            self.collection[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        try:
            self.collection[hash_key].remove(key)
        except ValueError:
            pass
        
    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        try:
            self.collection[hash_key].index(key)
        except ValueError:
            return False
        
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)