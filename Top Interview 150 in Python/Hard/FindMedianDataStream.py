class MedianFinder:
    def __init__(self):
        # two heaps: one for smaller half of numbers and one for larger half
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add the negative of the number to the max-heap representing the smaller half
        heapq.heappush(self.small, -1 * num)

        # if both heaps are non-empty and the top element of small heap is greater than top element of large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # pop the top element from small heap and push it to large heap to maintain balance
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # if small heap becomes larger than large heap by more than 1, rebalance them
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if large heap becomes larger than small heap by more than 1, rebalance them
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if small heap has more elements, return the top element of small heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # if large heap has more elements, return the top element of large heap
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # if both heaps have equal number of elements, return the average of their top elements
        return (-1 * self.small[0] + self.large[0]) / 2
