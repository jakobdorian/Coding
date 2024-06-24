class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipQueue = deque()
        res = 0

        for i in range(len(nums)):
            # remove flips that are out of current window
            if flipQueue and flipQueue[0] <= i:
                flipQueue.popleft()
            
            # determine if we need to flip the current bit
            if len(flipQueue) % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                # add the end of the current flip window to the queue
                flipQueue.append(i + k)
                res += 1
        # return the total number of flips
        return res
