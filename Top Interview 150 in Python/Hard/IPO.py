class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # create a list of tuples (capital, profit) from capital and profits lists
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        # convert minCapital list into a min-heap
        heapq.heapify(minCapital)
        # max-heap storing negative profits
        maxProfit = []
        # Iterate k times
        for i in range(k):
            # while there's available projects and the current capital is enough
            while minCapital and minCapital[0][0] <= w:
                # pop the project with the minimum capital requirement
                c, p = heapq.heappop(minCapital)
                # push the negative profit onto maxProfit heap
                heapq.heappush(maxProfit, -p)
            # if there are no available projects, break
            if not maxProfit:
                break
            # deduct the investment from capital
            w -= heapq.heappop(maxProfit)
        # return the remaining capital
        return w

# Time complexity:
# - Building minCapital: O(n), where n is the length of capital or profits list
# - Heapify operation: O(n)
# - For loop: O(k)
# - While loop inside the for loop: O(n), but overall it's O(n * k)
# - Pushing and popping from heaps: O(log n)
# Total time complexity: O(nlogn + klogn)
