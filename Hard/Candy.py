class Solution:
    def candy(self, ratings: List[int]) -> int:
        # fill in a array for candies with 1s
        candies = [1] * len(ratings)
        # skip first index as it doesn't have a neighbour
        # left to right
        for i in range(1, len(ratings)):
            # does this element have a > rating then the left?
            if ratings[i - 1] < ratings[i]:
                # needs more candy
                candies[i] = candies[i - 1] + 1
        # right to left (reverse), skip last index
        for i in range(len(ratings) - 2, -1, -1):
            # does the curr element have a > rating then the right?
            if ratings[i] > ratings[i + 1]:
                # needs for candy
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)