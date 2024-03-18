class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # get the size of the grid
        N = len(grid) 
        
        # counter to keep track of row frequencies
        rows = Counter()
        
        res = 0

        # count the frequency of each row
        for x in range(N):
            curr = " ".join(str(val) for val in grid[x]) # Convert the row to string
            rows[curr] += 1
        
        # check for equal pairs in columns
        for y in range(N):
            cols = []
            for x in range(N):
                cols.append(grid[x][y]) # Extracting column values
            curr = " ".join(str(val) for val in cols) # Convert the column to string

            # if the current column pattern is found in rows, add its frequency to result
            if curr in rows:
                res += rows[curr]
                
        return res
