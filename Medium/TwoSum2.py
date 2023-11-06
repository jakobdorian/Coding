class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        # go through array using two pointers
        while p1 < p2:
            curr = numbers[p1] + numbers[p2]
            if curr > target:
                p2 -= 1
            elif curr < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
        return []
