class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # a list with 0 added at the beginning and end to handle edge cases
        f = [0] + flowerbed + [0]

        # iterate through the flowerbed
        for i in range(1, len(f) -1):
            # check if current position and its adjacent positions are all empty
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                # place a flower at the current position
                f[i] = 1
                # decrement the count of remaining flowers to place
                n -= 1
        
        # check if all flowers have been placed
        return n <= 0
