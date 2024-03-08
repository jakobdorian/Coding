class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # create a counter to count occurrences of each number in nums
        c = Counter(nums)
        res = 0
        # set to keep track of visited numbers to avoid duplicate calculations
        visited = set()

        # iterate through the unique numbers in the counter
        for x in c:
            # check if the complement of the current number exists in the counter and has not been visited yet
            if x not in visited and (k - x) in c:
                # if the current number is the same as its complement, we can use half of its occurrences
                if x == (k-x):
                    res += c[x] // 2
                else:
                    # otherwise, we take the minimum occurrences of the current number and its complement
                    res += min(c[x], c[k-x])
                # mark both the current number and its complement as visited
                visited.add(x)
                visited.add(k-x)
        return res
        