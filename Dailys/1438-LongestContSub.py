class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        left, res = 0, 0

        for right in range(len(nums)):

            # maintain the max deque in current window
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # maintain the min deque in current window
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # check if the current window is valid
            while max_deque and min_deque and nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # remove elements that are out of the current window
                if max_deque and max_deque[0] < left:
                    max_deque.popleft()
                if min_deque and min_deque[0] < left:
                    min_deque.popleft()
            # update res with the length of the current valid window
            res = max(res, right - left + 1)
        
        return res
