class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # a variable to keep track of the current depth in the folder structure
        res = 0
        
        # iterate through each log entry
        for log in logs:
            if log == "./":
                # "./" means stay in the current directory, so no change in depth
                continue
            elif log == "../":
                # "../" means move up one directory level, but we cannot go above the root directory (depth 0)
                res = max(0, res - 1)
            else:
                # any other log entry means move into a new subdirectory, so increase the depth
                res += 1
        
        # return the final depth in the folder structure
        return res
        