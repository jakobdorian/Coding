class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # an empty dictionary to store the occurrences of each element
        res = {}

        # iterate through the input array
        for n in arr:
            # update the dictionary by incrementing the count for the current element
            res[n] = res.get(n, 0) + 1

        # check if the number of unique occurrences is equal to the number of unique counts
        # this is done by comparing the lengths of the dictionary values and a set created from those values
        # if the lengths are equal, it means each count occurs uniquely
        return len(res.values()) == len(set(res.values()))
