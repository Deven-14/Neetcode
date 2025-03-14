class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]
        
        # detect all the rotten bananas
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
        
        # convert good bananas connected to rotten layer
        def convert_to_rotten(queue, r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            if visited[r][c] or grid[r][c] == 0:
                return
            
            visited[r][c] = True
            queue.append((r, c))
        
        # get min time for bananas to rotten
        minutes = -1 if queue else 0 # accounts for no rotten bananas
        while queue:
            curr_level_queue = queue
            queue = deque()

            while curr_level_queue:
                r, c = curr_level_queue.popleft()
                grid[r][c] = 2
                convert_to_rotten(queue, r + 1, c)
                convert_to_rotten(queue, r - 1, c)
                convert_to_rotten(queue, r, c + 1)
                convert_to_rotten(queue, r, c - 1)
        
            minutes += 1
        
        # check if any good bananas are left
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return minutes

