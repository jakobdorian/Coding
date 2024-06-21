class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0  # left end of the sliding window
        window = 0  # current additional satisfied customers in the window
        max_window = 0  # maximum additional satisfied customers in any window
        satisfied = 0  # total satisfied customers without any grumpy customers

        # iterate through the customers array with 'right' as the right end of the window
        for right in range(len(customers)):
            # if the owner is grumpy at this time, add these customers to the window count
            if grumpy[right]:
                window += customers[right]
            else:
                # otherwise, these customers are always satisfied
                satisfied += customers[right]

            # ensure the window size does not exceed the given 'minutes'
            if right - left + 1 > minutes:
                # if the customer at 'left' was added to the window, remove them as we slide the window right
                if grumpy[left]:
                    window -= customers[left]
                # move the left end of the window to the right
                left += 1

            # update the maximum additional satisfied customers in any window
            max_window = max(window, max_window)

        # the result is the total of always satisfied customers plus the best window of additional satisfied customers
        return satisfied + max_window
