class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        h = []  # heap to maintain candidate indices and their corresponding costs

        # add initial candidate indices and their costs to the heap
        left = 0
        for i in range(candidates):
            heapq.heappush(h, (costs[left], left, 1))  # Add candidates from the left
            left += 1

        right = n - 1

        for i in range(candidates):
            # break if left index surpasses or equals right index
            if left > right:
                break
            heapq.heappush(h, (costs[right], right, -1))  # Add candidates from the right
            right -= 1

        # calculate the total cost by popping candidates from the heap
        res = 0
        for _ in range(k):
            c, _, flag = heapq.heappop(h)  # get the candidate with the lowest cost

            res += c  # add the cost to the total result
            if left <= right:
                if flag == 1:
                    heapq.heappush(h, (costs[left], left, 1))  # add next candidate from the left
                    left += 1
                else:
                    heapq.heappush(h, (costs[right], right, -1))  # Add next candidate from the right
                    right -= 1
        return res  # return the total cost
