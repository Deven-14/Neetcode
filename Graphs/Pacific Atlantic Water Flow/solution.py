class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        def dfs(r, c, visited, ocean):
            if visited[r][c]:
                return
            
            visited[r][c] = True
            ocean.add((r, c))
            
            if r+1 < ROWS and heights[r][c] <= heights[r+1][c]:
                dfs(r+1, c, visited, ocean)
            
            if r-1 >= 0 and heights[r][c] <= heights[r-1][c]:
                dfs(r-1, c, visited, ocean)
            
            if c+1 < COLS and heights[r][c] <= heights[r][c+1]:
                dfs(r, c+1, visited, ocean)
            
            if c-1 >= 0 and heights[r][c] <= heights[r][c-1]:
                dfs(r, c-1, visited, ocean)
        
        pacific, atlantic = set(), set()
        visited_pacific = [[False] * COLS for _ in range(ROWS)]
        visited_atlantic = [[False] * COLS for _ in range(ROWS)]

        for i in range(COLS):
            dfs(0, i, visited_pacific, pacific)
            dfs(ROWS-1, i, visited_atlantic, atlantic)
        
        for i in range(ROWS):
            dfs(i, 0, visited_pacific, pacific)
            dfs(i, COLS-1, visited_atlantic, atlantic)
        
        return list(pacific & atlantic)
        

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        def dfs(r, c, ocean, prev_height):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return
            
            if (r, c) in ocean or heights[r][c] < prev_height:
                return
            
            ocean.add((r, c))
            height = heights[r][c]
            
            dfs(r+1, c, ocean, height)
            dfs(r-1, c, ocean, height)
            dfs(r, c+1, ocean, height)
            dfs(r, c-1, ocean, height)
        
        pacific, atlantic = set(), set()
        for i in range(COLS):
            dfs(0, i, pacific, 0)
            dfs(ROWS-1, i, atlantic, 0)
        
        for i in range(ROWS):
            dfs(i, 0, pacific, 0)
            dfs(i, COLS-1, atlantic, 0)
        
        return list(pacific & atlantic)


# * for BFS solution, add the pacific (left and top) to a queue, and atlantic (right and bottom) to another queue
# * for those queues, keep adding the neighbors that are higher than the current cell
# * run throught the entire queues and save the cells higher than in lists or sets
# * return the intersection of the two
        