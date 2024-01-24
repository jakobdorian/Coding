class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dictionary to map digits to corresponding letters
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # base case
        if not digits:
            return []
        res = [""]
        # iterate through each digit in the input string
        for d in digits:
            # temporary list to store combinations for the current digit
            temp = []
            # iterate through each letter corresponding to the current digit
            for v in lookup[d]:
                # iterate through each existing combination in the result list
                for o in res:
                    # append the current letter to each existing combination
                    temp.append(o + v)
            # update the result list with the combinations for the current digit
            res = temp
        # return the final list of combinations
        return res
