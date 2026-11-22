class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find_parent(self, node):
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def connect(self, node_u, node_v):
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        if parent_u == parent_v:
            return
        
        if parent_u not in self.rank:
            self.rank[parent_u] = 0
        
        if parent_v not in self.rank:
            self.rank[parent_v] = 0
        
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else:
            self.rank[parent_v] += 1
            self.parent[parent_u] = parent_v

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        
        def sieve(limit: int) -> list:
            primes = [2]
            seen = set()
            for i in range(3, limit + 1, 2):
                if i in seen:
                    continue

                primes.append(i)

                for j in range(i * i, limit + 1, i):
                    seen.add(i)
            return primes
        
        limit = max(nums)
        primes = set(sieve(int(1e5)))
        

        dsu = DSU()
        n = len(nums)
        pool = {}

        for i in range(n):
            j = 2
            while j * j <= nums[i]:
                if nums[i] % j == 0:
                    a, b = j, nums[i] // j
                    if a not in pool:
                        pool[a] = i
                    else:
                        dsu.connect(pool[a], i)
                    if b not in pool:
                        pool[b] = i
                    else:
                        dsu.connect(pool[b], i)
                j += 1

            j = nums[i]
            if j not in pool:
                pool[j] = i
            else:
                dsu.connect(pool[j], i)
                pool[j] = i
        
        parent = dsu.find_parent(0)
        for i in range(1, n):
            if parent != dsu.find_parent(i):
                return False
        return True

