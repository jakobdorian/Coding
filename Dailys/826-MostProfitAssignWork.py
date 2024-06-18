class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # combine difficulty and profit into a list of tuples and sort them by difficulty
        jobs = sorted(zip(difficulty, profit))
        # sort the worker list to make it easier to match them with jobs
        worker.sort()

        max_profit = 0  # this will store the maximum profit we can achieve at each worker's skill level
        res = 0  # this will store the total maximum profit we can achieve
        j = 0  # pointer to traverse the jobs list
        n = len(jobs)  # total number of jobs available

        # iterate over each worker's skill level
        for w in worker:
            # check if the worker can take up the job by comparing their skill level with the job difficulty
            while j < n and w >= jobs[j][0]:
                # update max_profit to the highest profit achievable for the current and previous jobs
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            # add the best profit the current worker can achieve to the total result
            res += max_profit
        
        return res  # return the total maximum profit that all workers can achieve
