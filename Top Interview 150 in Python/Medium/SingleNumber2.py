class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        # iterate through keys and vals in the counter
        for k, v in count.items():
            # if the count is 1, it means this number is the single occurrence
            if v == 1:
                return k
                