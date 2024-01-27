class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # depth-first search function
        def dfs(row, excl_cells):
            # if not all rows are processed
            if row < n:
                # iterate over each column in the current row
                for col in range(n):
                    # check if the current cell is excluded (under attack)
                    if (row, col) in excl_cells:
                        continue
                    # calculate cells to exclude in the next rows
                    excl_subs = set()
                    r1 = r2 = r3 = row
                    c1 = c2 = c3 = col
                    # exclude cells in the same column
                    while r1 < n:
                        r1 += 1
                        excl_subs.add((r1, c1))
                    # exclude cells in the right diagonal
                    while c2 < n:
                        c2 += 1
                        r2 += 1
                        excl_subs.add((r2, c2))
                    # cxclude cells in the left diagonal
                    while c3 > 0:
                        c3 -= 1
                        r3 += 1
                        excl_subs.add((r3, c3))
                    # recursively call dfs for the next row with updated excluded cells
                    dfs(row + 1, excl_cells | excl_subs)
            else:
                # if all rows are processed, increment the result count
                self.res += 1
        dfs(0, set())
        return self.res
