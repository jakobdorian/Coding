class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # helper function to generate combinations
        def helper(start, combo):
            # if the combination reaches the desired length 'k', add it to the result
            if len(combo) == k:
                res.append(combo.copy())
                return 
            # iterate over the numbers from 'start' to 'n'
            for i in range(start, n + 1):
                # include the current number in the combination
                combo.append(i)
                # recursively call the helper function with the next index and updated combination
                helper(i+1, combo)
                # backtrack by removing the last added element to try other combinations
                combo.pop()
        # start generating combinations from index 1 with an empty initial combination
        helper(1, [])
        # return the list of combinations
        return res
        