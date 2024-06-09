class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum, res = 0, 0
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        # iterate over each number in the nums list
        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k
            # if this remainder has been seen before, it means there are subarrays that sum up to a multiple of k
            if remain in prefix_count:
                res += prefix_count[remain]
            prefix_count[remain] += 1
        # return the total count of subarrays with sum divisible by k
        return res
