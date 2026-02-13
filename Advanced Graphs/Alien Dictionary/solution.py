from collections import defaultdict
class Solution:

    def create_adj_list(self, words):
        adj = { c: set() for w in words for c in w }
        n = len(words)
        
        # create adj list
        prev_word = words[0]
        for i in range(1, n):
            word = words[i]

            n = min(len(prev_word), len(word))
            if len(prev_word) > len(word) and prev_word[:n] == word[:n]: # ["apple world", "apple"]
                return None
            
            for i in range(n):
                if prev_word[i] != word[i]:
                    adj[prev_word[i]].add(word[i])
                    break # first mis-matching char, it might not be present as well, ["apple", "apples"]
            
            prev_word = word

        return adj

    def detect_cycle(self, adj, cycle, node, order):
        if node in cycle:
            return cycle[node]
        
        cycle[node] = True
        for adj_node in adj[node]:
            if self.detect_cycle(adj, cycle, adj_node, order):
                return True
        
        cycle[node] = False
        order.append(node)
        return False

    def foreignDictionary(self, words: List[str]) -> str:
        # Topological sorting with cycle detection
        adj = self.create_adj_list(words)
        if not adj:
            return ""
        
        cycle = {}
        order = []
        for node in adj:
            if self.detect_cycle(adj, cycle, node, order):
                return ""

        return "".join(order[::-1])


# * we could do this using topological sort BFS too, 
# * in that case if there is cycle, then the order will not be equal to the number of nodes
# * so we can check if len(order) == len(adj), if not, then return ""


from collections import deque
class Solution:

    def create_adj_list(self, words):
        adj = { c: set() for w in words for c in w }
        indegrees = { c: 0 for c in adj }
        n = len(words)
        
        # create adj list
        prev_word = words[0]
        for i in range(1, n):
            word = words[i]

            n = min(len(prev_word), len(word))
            if len(prev_word) > len(word) and prev_word[:n] == word[:n]: # ["apple world", "apple"]
                return None, None
            
            for i in range(n):
                if prev_word[i] != word[i]:
                    if word[i] not in adj[prev_word[i]]:
                        indegrees[word[i]] += 1
                        adj[prev_word[i]].add(word[i])
                    break # first mis-matching char, it might not be present as well, ["apple", "apples"]
            
            prev_word = word

        return adj, indegrees

    def bfs(self, adj, indegrees):
        queue = deque([c for c, indegree in indegrees.items() if indegree == 0])
        order = []

        while queue:
            c = queue.popleft()
            order.append(c)

            for adj_c in adj[c]:
                indegrees[adj_c] -= 1
                if indegrees[adj_c] == 0:
                    queue.append(adj_c)
        
        if len(order) != len(adj):
            return None
        
        return order[::-1]


    def foreignDictionary(self, words: List[str]) -> str:
        # Topological sorting with cycle detection
        adj, indegrees = self.create_adj_list(words)
        if not adj:
            return ""
        
        order = self.bfs(adj, indegrees)
        if not order:
            return ""

        return "".join(order[::-1])
