from math import gcd

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        self.components -= 1
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DisjointSetUnion(n)

        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) > 1:
                    dsu.union(i, j)
                    if dsu.components == 1:
                        return True
        
        return False
        

# ! slower

from math import gcd
from collections import defaultdict

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [0] * n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:

    def get_primes(self, MAX, nums):
        p = 2
        p2 = p * p
        prime = [True] * (MAX + 1)
        num_primes = defaultdict(list)
        nums_set = set(nums)

        while p2 <= MAX:
            if prime[p]:
                for i in range(p2, MAX + 1, p):
                    prime[i] = False

            p += 1
            p2 = p * p
        
        for p in range(2, MAX + 1):
            if prime[p]:
                for num in range(p, MAX + 1, p):
                    if num in nums_set:
                        num_primes[num].append(p)
        
        return num_primes


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        MAX = max(nums)
        dsu = DisjointSetUnion(n + MAX + 1)

        num_to_primes = self.get_primes(MAX, nums)

        for i, num in enumerate(nums):
            for prime in num_to_primes[num]:
                dsu.union(i, n + prime)
        
        root = dsu.find(0)
        for i in range(n):
            if dsu.find(i) != root:
                return False

        return True


# ! slower       

from math import gcd
from collections import defaultdict

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:

    def get_primes(self, MAX, nums):
        p = 2
        p2 = p * p
        prime = [True] * (MAX + 1)
        primes_to_indexes = defaultdict(list)
        nums_to_idx = { num: i for i, num in enumerate(nums) }

        while p2 <= MAX:
            if prime[p]:
                for i in range(p2, MAX + 1, p):
                    prime[i] = False

            p += 1
            p2 = p * p
        
        for p in range(2, MAX + 1):
            if prime[p]:
                for num in range(p, MAX + 1, p):
                    if num in nums_to_idx:
                        primes_to_indexes[p].append(nums_to_idx[num])
        
        return primes_to_indexes # ordered dict


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = list(set(nums))
        n = len(nums)
        MAX = max(nums)
        dsu = DisjointSetUnion(n + MAX + 1)

        primes_to_indexes = self.get_primes(MAX, nums)

        for prime, indexes in primes_to_indexes.items():
            for idx in indexes:
                dsu.union(idx, n + prime)
        
            root = dsu.find(0)
            is_connected = True
            for i in range(n):
                if dsu.find(i) != root:
                    is_connected = False
                    break
            
            if is_connected:
                return True

        return False
        


from math import gcd
from collections import defaultdict

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        self.components -= 1
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:

    def get_primes(self, MAX, nums):
        p = 2
        p2 = p * p
        prime = [True] * (MAX + 1)
        primes_to_indexes = defaultdict(list)
        nums_to_idx = { num: i for i, num in enumerate(nums) }

        while p2 <= MAX:
            if prime[p]:
                for i in range(p2, MAX + 1, p):
                    prime[i] = False

            p += 1
            p2 = p * p
        
        for p in range(2, MAX + 1):
            if prime[p]:
                for num in range(p, MAX + 1, p):
                    if num in nums_to_idx:
                        primes_to_indexes[p].append(nums_to_idx[num])
        
        return primes_to_indexes # ordered dict


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = list(set(nums))
        n = len(nums)
        MAX = max(nums)
        dsu = DisjointSetUnion(n)

        primes_to_indexes = self.get_primes(MAX, nums)
        visited_primes = {}

        for prime, indexes in primes_to_indexes.items():
            for idx in indexes:
                if prime in visited_primes:
                    dsu.union(idx, visited_primes[prime])
                else:
                    visited_primes[prime] = idx
            
            if dsu.components == 1:
                return True

        return False
        


from math import gcd
from collections import defaultdict

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        self.components -= 1
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:

    def get_prime_factors(self, nums):
        p = 2
        p2 = p * p
        MAX = max(nums)
        spf = list(range(MAX + 1)) # smallest prime factor
        prime_factors = defaultdict(set)

        while p2 <= MAX:
            if spf[p] == p: # is prime
                for i in range(p2, MAX + 1, p):
                    if spf[i] == i:
                        spf[i] = p

            p += 1
            p2 = p * p
        
        for num in nums:
            x = num
            while x > 1:
                p = spf[x]
                prime_factors[num].add(p)
                while x % p == 0:
                    x //= p

        return prime_factors # ordered dict


    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = set(nums)
        n = len(nums)

        if 1 in nums:
            return False
        
        if n == 1:
            return True

        nums = list(set(nums))
        nums_to_idx = { num: i for i, num in enumerate(nums) }
        dsu = DisjointSetUnion(n)

        prime_factors = self.get_prime_factors(nums)
        prime_owner = {}

        for idx, num in enumerate(nums):
            for p in prime_factors[num]:
                if p in prime_owner:
                    dsu.union(idx, prime_owner[p])
                else:
                    prime_owner[p] = idx
            
            if dsu.components == 1:
                return True

        return False
        
